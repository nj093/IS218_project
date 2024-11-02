Project Documentation

The Calculator is created to handle with different commands and inputs and execute operations to give the result output to the user. The calculator uses pandas and numpy libraries to save environment variables to accept and handle multiple commands and give results realted to that.

Design Patterns: 

1. Fascade pattern: The historyManager class hides complex Pandas operations and provides a simple interface for saving, loading, and clearing history.
2. Command Pattern:  Used for organizing different operations like addCommand and SubtractCommand making the REPL modular and easier to extend.
3. Strategy Pattern: Can be used in the future if you need different algorithms for specific operations.