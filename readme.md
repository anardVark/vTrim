# vTrim
## About
This program allows you to trim the beginnings and endings off mp4 files. You can either trim a single video or an entire directory.
## Version Notes
### v0.0.6
```
> 01/18/2024
> Added output menu to see stdout read out but it just freeze while the trimming script is exectuted.
> Added tooltips to trim time inputs
> Removed custom title bar
> Window is now resizable
```
### v0.0.5
```
> 01/18/2024
> User-defined trim time
> Modified several exception cases for stability
```
### v0.0.4
```
> 01/17/2024
> Can trim single or full directories
```
## Planned Features
```
> User-defined output directory
> Move to multithreaded running to allow interaction while stripping the file.
> Add an advanced menu to contain User-defined output directory, Output Window, and User-defined trim time.
```
### Build to Exe Instructions
1. Update relevant file info in setup.py
2. In CMD -> ```Python setup.py build```