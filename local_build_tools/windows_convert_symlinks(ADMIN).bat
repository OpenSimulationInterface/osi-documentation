@ECHO OFF
SET Targetpath=..\.antora\modules\specification
SET Symlinkroot=..\..\..

mklink /D %Targetpath%\images %Symlinkroot%\content\_static\images

mklink /D %Targetpath%\pages %Symlinkroot%\content

@REM mklink /D %Targetpath%\partials %Symlinkroot%\_additional_content

@REM mklink /D %Targetpath%\attachments %Symlinkroot%\_attachments

PAUSE