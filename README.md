# TimeLoader2

early aces

# Mod Format

A typical mod might have the following structure:

```
mod_name.zip/
│
├── modmeta.tkml
├── autoapply.tkml
└── mod_files/
    ├── options-bottom.rpy
    ├── test.txt
    └── ... (other mod files)
```

### `modmeta.tkml`

#### Example:
```json
{
  "mod_name": "Sample Mod",
  "author": "Your Name",
  "version": "1.0",
  "mod_id": "test.example.modID",
  "description": "A sample mod demonstrating various functionalities."
}
```

#### Fields:
- `mod_name`: The name of the mod.
- `author`: Author's name or username.
- `version`: Version of the mod.
- `mod_id`: Mod ID for identification.
- `description`: Brief description of the mod's purpose or changes.

### `autoapply.tkml`

#### Example:
```json
[
  {
    "method": "addline_bottom",
    "file": "/game/options.rpy",
    "lines_source": "mod_files/options-bottom.rpy"
  },
  {
    "method": "replace_label",
    "file": "/game/scripts/act1.rpy",
    "old_label_name": "crash",
    "label_source": "mod_files/test.txt"
  },
  {
    "method": "addline_top",
    "file": "/easteregg.bat",
    "lines_source": "mod_files/test.txt"
  }
]
```

#### Fields:
- `method`: The method of modification (`addline_bottom`, `addline_top`, `replace_label`, etc.).
- `file`: Path to the target file within the game directory.
- `lines_source` or `label_source`: Path to the file containing lines or label content to add or replace.
- `old_label_name` (for `replace_label`): Name of the label to be replaced.

### Usage

1. Create a directory for your mod.
2. Add `modmeta.tkml` with mod details.
3. Include mod files in the `mod_files` directory.
4. Define modifications in `autoapply.tkml`.

# Code Injecting Methods

#### `addline_bottom`
- **Description**: Adds lines of code at the bottom of a specified file.
- **Parameters**:
  - `file`: Path to the file where lines are added.
  - `lines_source`: File containing lines to add.
- **Usage**:
  ```json
  {
    "method": "addline_bottom",
    "file": "/game/options.rpy",
    "lines_source": "options-bottom.rpy"
  }
  ```

#### `addline_top`
- **Description**: Adds lines of code at the top of a specified file.
- **Parameters**:
  - `file`: Path to the file where lines are added.
  - `lines_source`: File containing lines to add.
- **Usage**:
  ```json
  {
    "method": "addline_top",
    "file": "/easteregg.bat",
    "lines_source": "test.txt"
  }
  ```

#### `addline_safe`
- **Description**: Adds lines of code above the first defined label in a file.
- **Parameters**:
  - `file`: Path to the file where lines are added.
  - `lines_source`: File containing lines to add.
- **Usage**:
  ```json
  {
    "method": "addline_safe",
    "file": "/easteregg.bat",
    "lines_source": "test.txt"
  }
  ```

#### `replace_label`
- **Description**: Replaces an entire label block in a specified file.
- **Parameters**:
  - `file`: Path to the file where the label is replaced.
  - `old_label_name`: Name of the label to be replaced.
  - `label_source`: File containing the new label content.
- **Usage**:
  ```json
  {
    "method": "replace_label",
    "file": "/game/scripts/act1.rpy",
    "old_label_name": "crash",
    "label_source": "test.txt"
  }
  ```
