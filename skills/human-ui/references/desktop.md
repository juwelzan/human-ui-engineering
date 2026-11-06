# Desktop Development Progressive Reference

> **Quick-reference rules for Electron, Tauri & Flutter Desktop.**

- **Security & IPC**:
  - In Electron: Always set `contextIsolation: true` and `nodeIntegration: false`. Validate all IPC messages.
  - In Tauri: Restrict command permissions in `tauri.conf.json`.
- **Window Dragging**: In custom titlebars, add CSS `-webkit-app-region: drag` to draggable header regions and `no-drag` to buttons and search inputs.
- **Keyboard Shortcuts**: Support standard OS keybindings (`Cmd` on macOS vs `Ctrl` on Windows/Linux).
- **Offline First**: Use local persistence (SQLite, IndexedDB) with background synchronization.

See full guide in [`../../../frameworks/desktop.md`](../../../frameworks/desktop.md).
