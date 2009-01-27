#!/bin/bash

set -e

. /usr/share/opengl-games-utils/opengl-game-functions.sh

checkDriOK "Urban Terror"

if [ ! -f ~/.q3a/q3ut4/zpak000.pk3 ]; then
  set +e
  /usr/share/autodl/AutoDL.py /usr/share/quake3/urbanterror.autodlrc
  STATUS=$?
  set -e
  # status 2 means download was ok, but the user choice not to start the game
  if [ "$STATUS" = "0" -o "$STATUS" = "2" ]; then
    pushd ~/.q3a > /dev/null
    unzip -qq -u UrbanTerror_41_FULL.zip
    # remove any old versions (if present) otherwise the mv fails
    rm -fr q3ut4
    mv UrbanTerror/q3ut4 .
    rm -r UrbanTerror UrbanTerror_41_FULL.zip
    popd > /dev/null
  fi
  if [ "$STATUS" != "0" ]; then
    exit $STATUS
  fi
fi

exec quake3 +set fs_game q3ut4 +set com_hunkMegs 256 "$@"
