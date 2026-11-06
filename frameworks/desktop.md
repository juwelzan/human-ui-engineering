# Desktop UI Engineering Guide (Electron, Tauri & Flutter Desktop)

> Practical engineering guide for building native and cross-platform desktop applications for macOS, Windows, and Linux.

---

## 1. Desktop Paradigms vs. Web Interfaces

Desktop applications differ fundamentally from browser tabs:
- **Window Management**: Multiple windows, modal dialogs, titlebars, minimizing to system tray, remembering window coordinates and maximized states.
- **Input Modes**: Mouse, trackpad, physical keyboards with extensive shortcuts (`Cmd/Ctrl+S`, `Cmd/Ctrl+Z`), right-click context menus.
- **Hardware Integration**: Local filesystem access, offline-first architectures, low-level OS notifications, multi-monitor setups.
- **Process Boundaries**: Strict separation between the **Main / Host Process** (Node.js/Rust) and the **Renderer UI Process** (DOM / Webview / Canvas).

---

## 2. Framework Comparison: Electron vs. Tauri vs. Flutter Desktop

| Framework | UI Technology | Backend / Core | Binary Size | Memory Footprint | Best Used For |
|---|---|---|---|---|---|
| **Tauri** | Web (React/Vue/HTML) | Rust / OS WebView (WebKit/Webview2) | Ultra-light (< 15MB) | Minimal (~30MB–60MB) | Modern, secure, memory-efficient desktop utilities |
| **Electron** | Web (React/Vue/HTML) | Node.js + Bundled Chromium | Heavy (~80MB–120MB) | High (~150MB–300MB) | Deep Node.js ecosystem dependencies, complex rich media |
| **Flutter Desktop** | Flutter Widgets | Dart + C++ Native Runner | Compact (~30MB) | Moderate (~60MB–90MB) | Pixel-perfect parity with Flutter mobile applications |

---

## 3. Desktop UI/UX Conventions

### 1. Titlebar & Window Chrome
- **macOS**: Integrate with native traffic light buttons (Close, Minimize, Maximize); support translucent vibrancy (`visualEffectView`).
- **Windows**: Respect system caption buttons and Windows 11 snap layouts.
- **Frameless Windows**: If designing a custom titlebar, declare a designated drag region:
  ```css
  .titlebar-drag-region {
    -webkit-app-region: drag;
  }
  .titlebar-no-drag {
    -webkit-app-region: no-drag;
  }
  ```

### 2. Comprehensive Keyboard Shortcuts
Every desktop app must provide standard keyboard accelerators:
- Save: `Cmd+S` (macOS) / `Ctrl+S` (Windows/Linux)
- Find: `Cmd+F` / `Ctrl+F`
- Undo / Redo: `Cmd+Z` / `Cmd+Shift+Z`
- Close Window: `Cmd+W` / `Ctrl+W`
- Global Shortcut Navigation: Quick search palette (`Cmd+K` / `Ctrl+K`)

### 3. Context Menus (Right-Click)
- Never display standard browser context menus ("Inspect Element", "View Source") in production desktop apps.
- Implement contextual right-click actions (Copy, Paste, Duplicate, Delete) mapped to current selection.

---

## 4. Security & IPC Boundary Discipline

Never expose raw OS system privileges directly to the UI rendering context:

### Electron Security Rule:
```typescript
// main.ts
const mainWindow = new BrowserWindow({
  webPreferences: {
    contextIsolation: true,  // MANDATORY: Isolates preload scripts from DOM
    nodeIntegration: false,   // MANDATORY: Prevents DOM from calling require('fs')
    sandbox: true,
    preload: path.join(__dirname, 'preload.js'),
  },
});
```

### Typed Inter-Process Communication (IPC):
```typescript
// preload.ts (Expose narrow, explicit APIs via contextBridge)
contextBridge.exposeInMainWorld('desktopAPI', {
  saveFile: (content: string) => ipcRenderer.invoke('save-file', content),
});
```

---

## 5. Memory Management & Multi-Window Lifecycle

1. **Window Close vs. App Quit (macOS)**: On macOS, clicking the red close button should hide/close the window, but the app should remain active in the dock until explicitly terminated (`Cmd+Q`).
2. **Releasing Hidden Windows**: Detach listeners and pause animations on minimized or hidden windows to consume 0% idle CPU.
3. **Window State Persistence**: Save window geometry (`x`, `y`, `width`, `height`, `isMaximized`) to local settings on resize, and restore upon next launch.

---

## 6. Common Mistakes to Avoid

1. **Treating Desktop Like a Mobile Web Page**: Forgetting right-click menus, lacking keyboard shortcuts, and rendering full-screen mobile hamburger menus on a 32-inch monitor.
2. **Blocking the UI Renderer with Heavy Local File I/O**: Reading a 500MB file synchronously in the UI thread freezes the entire application. Offload disk I/O to background workers or the host process.
3. **Missing Offline Handling**: Assuming desktop machines always have internet; desktop software must handle offline launch gracefully.

---

## 7. Related Documentation

- Framework Selection: [framework-selection.md](framework-selection.md)
- Framework Isolation: [README.md](README.md)
- Security Fundamentals: [../engineering/security.md](../engineering/security.md)
- Cross-Platform Standards: [../engineering/cross-platform.md](../engineering/cross-platform.md)
