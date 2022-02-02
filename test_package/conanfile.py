import os

from conans import ConanFile, CMake, tools


class FhSimTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths", "cmake_find_package"

    def build(self):
        cmake = self._configure_cmake()
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", src="bin")
        self.copy("*.dylib*", src="lib")
        self.copy('*.so*', src='lib')

    _cmake = None

    def _configure_cmake(self):
        if self._cmake == None:
            self._cmake = CMake(self)
            self._cmake.configure()
        return self._cmake

    def test(self):
        if self.settings.compiler == "Visual Studio":
            self.run(os.path.join(self.build_folder, str(self.settings.build_type), "test.exe"))
        else:
            self.run(os.path.join(self.build_folder, "test"))
