import info
import kdedefaults as kd

class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]kde:%s|%s|' % (self.package, kd.kdebranch)
        for ver in ['0', '1', '2', '3', '4', '5']:
            self.targets[kd.kdeversion + ver] = "http://download.kde.org/stable/" + kd.kdeversion + ver + "/src/" + self.package + "-" + kd.kdeversion + ver + ".tar.xz"
            self.targetInstSrc[kd.kdeversion + ver] = self.package + '-' + kd.kdeversion + ver

        self.patchToApply['4.10.2'] = [('gwenview-4.10.2-allow-compilation-with-jpeg9.patch', 1), ('replace-usage-of-unportable-mkdtemp-with-KTempDir-update.patch', 1)]

        self.shortDescription = "Image viewer for KDE"
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.dependencies['kde/kde-baseapps'] = 'default'
        self.dependencies['kde/libkipi'] = 'default' 
        self.dependencies['win32libs/exiv2'] = 'default'
        self.dependencies['win32libs/jpeg'] = 'default'
   


from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )

if __name__ == '__main__':
    Package().execute()