#!/bin/sh
exec quake3 +set fs_game q3ut4 +set com_hunkMegs 256 ${1:+"$@"}
