import os
import zlib

from CraftCore import CraftCore
from CraftConfig import craftSettings
from CraftOS.OsDetection import OsDetection


class CraftShortPath(object):
    _useShortpaths = OsDetection.isWin() and craftSettings.getboolean("ShortPath", "EnableJunctions", False)
    _shortPaths = {}

    def __init__(self, path, createShortPath=None) -> None:
        self.longPath = path
        self._shortPath = None
        if not createShortPath:
            self._createShortPathLambda = CraftShortPath._createShortPath
        else:
            self._createShortPathLambda = createShortPath

    def path(self, condition):
        return self.shortPath if condition else self.longPath

    @property
    def shortPath(self) -> str:
        if self._shortPath:
            return self._shortPath
        self._shortPath = CraftShortPath._shortPaths.get(self.longPath, None)
        if not self._shortPath:
            self._shortPath = self._createShortPathLambda(self.longPath)
            CraftShortPath._shortPaths[self.longPath] = self._shortPath
        CraftCore.debug.log.debug(f"Mapped \n"
                            f"{self.longPath} to\n"
                            f"{self._shortPath}, gained {len(self.longPath) - len(self._shortPath)}")
        return self._shortPath

    @staticmethod
    def _createShortPath(longPath) -> str:
        import utils
        if not CraftShortPath._useShortpaths:
            return longPath
        if not os.path.isdir(CraftCore.standardDirs.junctionsDir()):
            os.makedirs(CraftCore.standardDirs.junctionsDir())
        path = os.path.join(CraftCore.standardDirs.junctionsDir(), str(zlib.crc32(bytes(longPath, "UTF-8"))))
        if len(longPath) < len(path):
            CraftCore.debug.log.info(f"Using junctions for {longPath} wouldn't save characters returning original path")
            return longPath
        if not os.path.isdir(path):
            if not os.path.isdir(longPath):
                os.makedirs(longPath)
            # note: mklink is a CMD command => needs shell
            if not utils.system(["mklink", "/J", path, longPath], shell=True):
                CraftCore.debug.log.critical(f"Could not create shortpath {path}, for {longPath}")
                return longPath
        else:
            if not os.path.samefile(path, longPath):
                CraftCore.debug.log.critical(f"Existing short path {path}, did not match {longPath}")
                return longPath
        return path
