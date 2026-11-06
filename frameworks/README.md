# Parallel Framework Architecture & Isolation Standards

> Architectural boundaries, selection criteria, and framework isolation rules across Human UI Engineering.

---

## 1. The Critical Framework Isolation Rule

> **A framework module must NEVER impose its implementation conventions on another framework.**

In multi-platform software engineering, mixing framework paradigms leads to broken mental models, unmaintainable abstractions, and severe runtime performance degradation:
- **Flutter** uses Widgets, `BuildContext`, Dart streams, and Skia/Impeller rendering.
- **React** uses Functional Components, Hooks, JSX, and the React reconciliation model.
- **Next.js** uses React Server Components (RSC), App Router streaming, and Edge runtimes.
- **Vue** uses Single File Components (`.vue`), the Composition API, Reactivity (`ref`, `reactive`), and Pinia.
- **Angular** uses TypeScript Classes, Signals, Dependency Injection, RxJS, and Zone.js / Zoneless change detection.
- **React Native** uses React paradigms mapped to native platform host views via the New Architecture (Fabric & TurboModules).
- **Native Android** uses Kotlin, Jetpack Compose, ViewModels, and Android OS lifecycles.
- **Native iOS** uses Swift, SwiftUI, Observation (`@Observable`), and Apple Human Interface Guidelines.
- **Modern Web** uses Semantic HTML5, CSS Custom Properties, Container Queries, and Web Components.
- **Desktop Development** uses Electron, Tauri, or native windowing runtimes.
- **Backend Development** uses Node.js, Python, Go, Java, or Rust with layered 3-tier architecture and asynchronous worker queues.
- **API Development** uses REST, GraphQL, gRPC, WebSockets, OpenAPI schemas, and cursor-based pagination.
- **Database Engineering** uses PostgreSQL, MySQL, SQLite, MongoDB, or Redis with zero-downtime expand/contract migrations.

Never recommend Flutter-specific solutions (e.g. `const` constructors or BLoC) for React projects. Never recommend React-specific solutions (e.g. `useEffect` or JSX) for Flutter or Android projects.

---

## 2. Framework Directory Map

| Framework Module | Primary Target | Core Runtime / Language | Link |
|---|---|---|---|
| **Flutter** | iOS, Android, Desktop, Web | Dart / Impeller / Skia | [flutter.md](flutter.md) |
| **React** | Web SPAs, Desktop | TypeScript / React / Vite | [react.md](react.md) |
| **Next.js** | Web with SSR & SEO | TypeScript / App Router / RSC | [nextjs.md](nextjs.md) |
| **Vue.js** | Web SPAs, Nuxt | TypeScript / Composition API / Pinia | [vue.md](vue.md) |
| **Angular** | Enterprise Web | TypeScript / Signals / Standalone Components | [angular.md](angular.md) |
| **React Native** | Mobile iOS & Android | TypeScript / Fabric / TurboModules | [react-native.md](react-native.md) |
| **Native Android** | Android OS, Wear OS, Auto | Kotlin / Jetpack Compose / Coroutines | [native-android.md](native-android.md) |
| **Native iOS** | iOS, iPadOS, macOS, watchOS | Swift / SwiftUI / Observation | [native-ios.md](native-ios.md) |
| **Modern Web** | Standard Browsers | HTML5 / CSS3 / Vanilla JS / Web Components | [web.md](web.md) |
| **Desktop Development** | macOS, Windows, Linux | Electron / Tauri / Native Desktop | [desktop.md](desktop.md) |
| **Backend Development** | Cloud Services & Microservices | Node.js, Python, Go, Java, Rust | [backend.md](backend.md) |
| **API Development** | Distributed Systems & Clients | REST, GraphQL, gRPC, WebSockets | [api.md](api.md) |
| **Database Engineering** | Persistence & Data Caching | PostgreSQL, MySQL, SQLite, MongoDB, Redis | [database.md](database.md) |

---

## 3. Monorepo Boundary Discipline

When multiple frameworks coexist in the same repository (e.g. a Next.js web portal and a Flutter mobile app inside an Nx or Turborepo monorepo):
1. **Identify the exact directory boundary** of the active subproject.
2. **Apply only the relevant framework module** to that directory.
3. Keep shared business logic in pure, framework-agnostic packages (TypeScript or protobuf/OpenAPI models).
4. Never cross-contaminate styling systems (e.g. forcing Tailwind utility classes inside Flutter).

---

## 4. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Framework Selection Matrix: [framework-selection.md](framework-selection.md)
- Universal Architecture: [../core/architecture.md](../core/architecture.md)

