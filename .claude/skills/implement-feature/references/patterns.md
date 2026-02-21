# Implementation Patterns

Reference patterns for implementing features in the Reflow codebase.

---

## Feature Module Pattern

### Directory Structure

```typescript
// features/{feature-name}/index.ts
// Only export public API

// Components (for use in routes)
export { FeatureList } from './components/FeatureList';
export { FeaturePage } from './components/FeaturePage';

// Hooks (for cross-feature use)
export { useFeature } from './hooks/useFeature';

// Types (for type sharing)
export type { Feature, CreateFeatureInput } from './types';

// Schemas (for validation sharing)
export { featureSchema, createFeatureSchema } from './schemas/feature.schema';
```

---

## Zod Schema Pattern

```typescript
// schemas/feature.schema.ts
import { z } from 'zod';

// Base schema with all fields
export const featureSchema = z.object({
  id: z.string().uuid(),
  name: z.string().min(1).max(100),
  description: z.string().max(500).optional(),
  status: z.enum(['active', 'archived', 'draft']),
  createdAt: z.coerce.date(),
  updatedAt: z.coerce.date(),
});

// Create input (omit auto-generated fields)
export const createFeatureSchema = featureSchema.omit({
  id: true,
  createdAt: true,
  updatedAt: true,
});

// Update input (all fields optional except id)
export const updateFeatureSchema = createFeatureSchema.partial();

// Type inference
export type Feature = z.infer<typeof featureSchema>;
export type CreateFeatureInput = z.infer<typeof createFeatureSchema>;
export type UpdateFeatureInput = z.infer<typeof updateFeatureSchema>;
```

---

## TanStack Query Pattern

### Query Hook

```typescript
// api/useFeatures.ts
import { useQuery } from '@tanstack/react-query';
import { apiClient } from '@/lib/api-client';
import type { Feature } from '../types';

export const featureKeys = {
  all: ['features'] as const,
  lists: () => [...featureKeys.all, 'list'] as const,
  list: (filters: string) => [...featureKeys.lists(), { filters }] as const,
  details: () => [...featureKeys.all, 'detail'] as const,
  detail: (id: string) => [...featureKeys.details(), id] as const,
};

export function useFeatures(filters?: { status?: string }) {
  return useQuery({
    queryKey: featureKeys.list(JSON.stringify(filters)),
    queryFn: async () => {
      const { data } = await apiClient.get<Feature[]>('/api/features', {
        params: filters,
      });
      return data;
    },
  });
}

export function useFeature(id: string) {
  return useQuery({
    queryKey: featureKeys.detail(id),
    queryFn: async () => {
      const { data } = await apiClient.get<Feature>(`/api/features/${id}`);
      return data;
    },
    enabled: !!id,
  });
}
```

### Mutation Hook

```typescript
// api/useCreateFeature.ts
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '@/lib/api-client';
import { featureKeys } from './useFeatures';
import type { CreateFeatureInput, Feature } from '../types';

export function useCreateFeature() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (input: CreateFeatureInput) => {
      const { data } = await apiClient.post<Feature>('/api/features', input);
      return data;
    },
    onSuccess: () => {
      // Invalidate list queries
      queryClient.invalidateQueries({ queryKey: featureKeys.lists() });
    },
  });
}
```

---

## Component Pattern

### List Component

```typescript
// components/FeatureList.tsx
import { Card, CardContent, CardHeader, CardTitle } from '@reflow/ui';
import { useFeatures } from '../api/useFeatures';
import { FeatureCard } from './FeatureCard';
import { FeatureEmptyState } from './FeatureEmptyState';
import { FeatureListSkeleton } from './FeatureListSkeleton';

interface FeatureListProps {
  filters?: { status?: string };
}

export function FeatureList({ filters }: FeatureListProps) {
  const { data: features, isLoading, error } = useFeatures(filters);

  if (isLoading) {
    return <FeatureListSkeleton />;
  }

  if (error) {
    return (
      <Card>
        <CardContent className="p-6">
          <p className="text-destructive">Failed to load features</p>
        </CardContent>
      </Card>
    );
  }

  if (!features?.length) {
    return <FeatureEmptyState />;
  }

  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      {features.map((feature) => (
        <FeatureCard key={feature.id} feature={feature} />
      ))}
    </div>
  );
}
```

### Card Component

```typescript
// components/FeatureCard.tsx
import { Card, CardContent, CardHeader, CardTitle } from '@reflow/ui';
import { Badge } from '@reflow/ui';
import { Link } from '@tanstack/react-router';
import type { Feature } from '../types';

interface FeatureCardProps {
  feature: Feature;
}

export function FeatureCard({ feature }: FeatureCardProps) {
  return (
    <Link to="/features/$featureId" params={{ featureId: feature.id }}>
      <Card className="hover:border-primary transition-colors cursor-pointer">
        <CardHeader className="pb-2">
          <div className="flex items-center justify-between">
            <CardTitle className="text-lg">{feature.name}</CardTitle>
            <Badge variant={feature.status === 'active' ? 'default' : 'secondary'}>
              {feature.status}
            </Badge>
          </div>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground line-clamp-2">
            {feature.description || 'No description'}
          </p>
        </CardContent>
      </Card>
    </Link>
  );
}
```

---

## Zustand Store Pattern

```typescript
// stores/feature.store.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface FeatureUIState {
  // UI-only state
  viewMode: 'grid' | 'list';
  selectedIds: Set<string>;

  // Actions
  setViewMode: (mode: 'grid' | 'list') => void;
  toggleSelection: (id: string) => void;
  clearSelection: () => void;
}

export const useFeatureStore = create<FeatureUIState>()(
  persist(
    (set) => ({
      viewMode: 'grid',
      selectedIds: new Set(),

      setViewMode: (mode) => set({ viewMode: mode }),

      toggleSelection: (id) =>
        set((state) => {
          const newSelection = new Set(state.selectedIds);
          if (newSelection.has(id)) {
            newSelection.delete(id);
          } else {
            newSelection.add(id);
          }
          return { selectedIds: newSelection };
        }),

      clearSelection: () => set({ selectedIds: new Set() }),
    }),
    {
      name: 'feature-ui-storage',
      partialize: (state) => ({ viewMode: state.viewMode }),
    }
  )
);

// Selectors
export const selectViewMode = (state: FeatureUIState) => state.viewMode;
export const selectSelectedCount = (state: FeatureUIState) => state.selectedIds.size;
```

---

## Route Pattern

```typescript
// app/routes/features/index.tsx
import { createFileRoute } from '@tanstack/react-router';
import { z } from 'zod';
import { FeatureList } from '@/features/feature/components/FeatureList';

const searchSchema = z.object({
  status: z.enum(['active', 'archived', 'draft']).optional(),
  page: z.number().default(1),
});

export const Route = createFileRoute('/features/')({
  validateSearch: searchSchema,
  component: FeaturesPage,
});

function FeaturesPage() {
  const { status, page } = Route.useSearch();

  return (
    <div className="container py-6">
      <h1 className="text-2xl font-bold mb-6">Features</h1>
      <FeatureList filters={{ status }} />
    </div>
  );
}
```

---

## Form Pattern

```typescript
// components/FeatureForm.tsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { Button, Input, Textarea } from '@reflow/ui';
import { createFeatureSchema, type CreateFeatureInput } from '../schemas/feature.schema';
import { useCreateFeature } from '../api/useCreateFeature';

interface FeatureFormProps {
  onSuccess?: () => void;
}

export function FeatureForm({ onSuccess }: FeatureFormProps) {
  const createFeature = useCreateFeature();

  const form = useForm<CreateFeatureInput>({
    resolver: zodResolver(createFeatureSchema),
    defaultValues: {
      name: '',
      description: '',
      status: 'draft',
    },
  });

  const onSubmit = async (data: CreateFeatureInput) => {
    await createFeature.mutateAsync(data);
    form.reset();
    onSuccess?.();
  };

  return (
    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label htmlFor="name" className="text-sm font-medium">
          Name
        </label>
        <Input
          id="name"
          {...form.register('name')}
          aria-invalid={!!form.formState.errors.name}
        />
        {form.formState.errors.name && (
          <p className="text-sm text-destructive mt-1">
            {form.formState.errors.name.message}
          </p>
        )}
      </div>

      <div>
        <label htmlFor="description" className="text-sm font-medium">
          Description
        </label>
        <Textarea
          id="description"
          {...form.register('description')}
        />
      </div>

      <Button type="submit" disabled={createFeature.isPending}>
        {createFeature.isPending ? 'Creating...' : 'Create Feature'}
      </Button>
    </form>
  );
}
```

---

## Testing Pattern

```typescript
// components/FeatureList.test.tsx
import { render, screen } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { describe, it, expect, vi } from 'vitest';
import { FeatureList } from './FeatureList';

// Mock the API hook
vi.mock('../api/useFeatures', () => ({
  useFeatures: vi.fn(),
}));

import { useFeatures } from '../api/useFeatures';

const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } },
  });
  return ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
};

describe('FeatureList', () => {
  it('shows loading state', () => {
    (useFeatures as vi.Mock).mockReturnValue({
      data: undefined,
      isLoading: true,
      error: null,
    });

    render(<FeatureList />, { wrapper: createWrapper() });

    expect(screen.getByTestId('feature-list-skeleton')).toBeInTheDocument();
  });

  it('shows empty state when no features', () => {
    (useFeatures as vi.Mock).mockReturnValue({
      data: [],
      isLoading: false,
      error: null,
    });

    render(<FeatureList />, { wrapper: createWrapper() });

    expect(screen.getByText(/no features/i)).toBeInTheDocument();
  });

  it('renders feature cards', () => {
    (useFeatures as vi.Mock).mockReturnValue({
      data: [
        { id: '1', name: 'Feature 1', status: 'active' },
        { id: '2', name: 'Feature 2', status: 'draft' },
      ],
      isLoading: false,
      error: null,
    });

    render(<FeatureList />, { wrapper: createWrapper() });

    expect(screen.getByText('Feature 1')).toBeInTheDocument();
    expect(screen.getByText('Feature 2')).toBeInTheDocument();
  });
});
```
