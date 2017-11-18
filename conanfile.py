from conans import ConanFile, CMake, tools

class lexerConan(ConanFile):
    name = "lexer"
    version = "1.1.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False", "gtest:shared=False"
    generators = "cmake"
    build_policy = "missing"
    requires = 'gtest/1.8.0@lasote/stable', 'cereal/1.2.2@sunxfancy/stable', 'estring/1.2.2@sunxfancy/ci'
    exports = "*"
    
    def build(self):
        shared = {"BUILD_SHARED_LIBS": self.options.shared}
        cmake = CMake(self)
        cmake.configure(defs=shared)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("LICENSE", dst=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]
