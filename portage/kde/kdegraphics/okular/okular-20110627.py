import info
import kdedefaults as kd

class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]kde:%s|%s|' % (self.package, kd.kdebranch)
        for ver in ['0', '1', '2', '3', '4', '5']:
            self.targets[kd.kdeversion + ver] = "http://download.kde.org/stable/" + kd.kdeversion + ver + "/src/" + self.package + "-" + kd.kdeversion + ver + ".tar.xz"
            self.targetInstSrc[kd.kdeversion + ver] = self.package + '-' + kd.kdeversion + ver
            
        self.patchToApply["4.10.0"] = [("okular-4.10.0-20130219.diff", 1)]
        self.patchToApply["4.10.1"] = [("okular-4.10.0-20130219.diff", 1)]
        self.patchToApply["4.10.2"] = [("okular-4.10.0-20130219.diff", 1)]

        self.shortDescription = "KDE document viewer"
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.buildDependencies['win32libs/chm'] = 'default'
        self.dependencies['kde/kdelibs'] = 'default'
        self.dependencies['kdesupport/qca'] = 'default'
        self.dependencies['kdesupport/poppler'] = 'default'
        self.dependencies['kdesupport/qimageblitz'] = 'default'
        self.dependencies['win32libs/tiff'] = 'default'
        self.dependencies['win32libs/djvu'] = 'default'
        self.dependencies['win32libs/zlib'] = 'default'
        self.dependencies['win32libs/freetype'] = 'default'
        self.dependencies['win32libs/libspectre'] = 'default'
        self.runtimeDependencies['kde/kde-runtime'] = 'default'

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )

if __name__ == '__main__':
    Package().execute()