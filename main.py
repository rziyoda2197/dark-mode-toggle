import json
import os

class DarkModeToggle:
    def __init__(self):
        self.localStorageKey = 'darkMode'

    def getDarkMode(self):
        if os.path.exists('dark_mode.json'):
            with open('dark_mode.json', 'r') as f:
                return json.load(f)
        else:
            return False

    def setDarkMode(self, value):
        with open('dark_mode.json', 'w') as f:
            json.dump(value, f)

    def toggleDarkMode(self):
        darkMode = self.getDarkMode()
        self.setDarkMode(not darkMode)
        return not darkMode

def main():
    darkModeToggle = DarkModeToggle()

    def toggleDarkMode():
        darkMode = darkModeToggle.toggleDarkMode()
        if darkMode:
            print("Dark mode enabled")
        else:
            print("Dark mode disabled")

    toggleDarkMode()
    print(darkModeToggle.getDarkMode())

if __name__ == "__main__":
    main()
```

```javascript
// dark_mode.js
class DarkModeToggle {
  constructor() {
    this.localStorageKey = 'darkMode';
  }

  getDarkMode() {
    const storedDarkMode = localStorage.getItem(this.localStorageKey);
    return storedDarkMode === 'true';
  }

  setDarkMode(value) {
    localStorage.setItem(this.localStorageKey, value);
  }

  toggleDarkMode() {
    const darkMode = this.getDarkMode();
    this.setDarkMode(!darkMode);
    return !darkMode;
  }
}

export default DarkModeToggle;
```

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import DarkModeToggle from './dark_mode';

function App() {
  const [darkMode, setDarkMode] = useState(DarkModeToggle().getDarkMode());

  const toggleDarkMode = () => {
    const newDarkMode = DarkModeToggle().toggleDarkMode();
    setDarkMode(newDarkMode);
  };

  useEffect(() => {
    const storedDarkMode = DarkModeToggle().getDarkMode();
    setDarkMode(storedDarkMode);
  }, []);

  return (
    <div>
      <button onClick={toggleDarkMode}>
        {darkMode ? 'Dark mode' : 'Light mode'}
      </button>
    </div>
  );
}

export default App;
