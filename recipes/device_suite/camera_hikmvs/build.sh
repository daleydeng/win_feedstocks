name=camera_hikmvs
mkdir -p $PREFIX/{bin/$name,include/$name,lib}
base_d=v$PKG_VERSION/linux-$ARCH
cp -ar $base_d/include/* $PREFIX/include/$name/
cp -ar $base_d/lib/*.so* $PREFIX/lib/
cp -ar $base_d/bin/* $PREFIX/bin/$name/
rm -rf $PREFIX/bin/$name/tmp
