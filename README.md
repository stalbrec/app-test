## pyCharm setup on Windows
- when opening Terminal in pyCharm one can be confronted with some error about missing authorization:
    ```
    Activate.ps1 cannot be loaded because running scripts is 
    disabled on this system. For more information, see about_Execution_Policies at 
    ```
  - Fix with following from [this answer](https://stackoverflow.com/a/67553273)
    ```commandline
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
    ```