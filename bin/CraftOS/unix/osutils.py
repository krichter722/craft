import CraftOS.OsUtilsBase
import CraftDebug
import shutil
import os
import sys

class OsUtils(CraftOS.OsUtilsBase.OsUtilsBase):

    @staticmethod
    def rm(path, force=False):
        CraftDebug.debug("deleting file %s" % path, 3)
        try:
            os.remove(path)
            return True
        except OSError as e:
            CraftDebug.warning("could not delete file %s: %s" % (path, e))
            return False

    @staticmethod
    def rmDir(path, force=False):
        CraftDebug.debug("deleting directory %s" % path, 3)
        try:
            shutil.rmtree(path)
            return True
        except OSError:
            return OsUtils.rm(path, force)
        return False

    @staticmethod
    def isLink(path):
        return os.path.islink(path)

    @staticmethod
    def removeReadOnlyAttribute(path):
        return False

    @staticmethod
    def setConsoleTitle(title):
         # TODO: http://www.faqs.org/docs/Linux-mini/Xterm-Title.html
        #sys.stdout.write( "\033]2;%s\007" % title)
        #sys.stdout.flush()
        return True