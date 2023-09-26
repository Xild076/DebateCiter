import cx_Freeze

exec_options = {
    "packages": [],
    "include_files": [],
    "excludes": ["multiprocessing"],
}

executables = [
    cx_Freeze.Executable(
        "C:/Users/harry/PycharmProjects/Debate/pain.py",
        base="Win32GUI",  # Use "Win32GUI" to create a GUI application
    )
]

cx_Freeze.setup(
    name="Debate suff",
    version="1.0",
    description="ye :D",
    options={"build_exe": exec_options},
    executables=executables
)
