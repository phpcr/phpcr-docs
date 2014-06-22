#!/usr/bin/bash
# This script will convert the JCR-SQL2 specification to restructured text.
# Note that the HTML file has been generated from the original DOC file.
# Note also that the conversion is not perfect, in particular images are not
# converted.

FILENAME=jcr-283.rst
TMPFILENAME=jcr-283.rst.tmp

echo "Converting HTML to RST"
echo "======================"
echo ""
echo "... wait ..."
pandoc -f html -t rst -o $FILENAME jcr-spec.html  +RTS -K18388608 -RTS
echo "done"

echo ""
echo "Postprocessing"
echo "=============="
echo ""

echo "- Removing first 16 lines"
sed -i '1,16d' $FILENAME

echo "- Removing original TOC"
sed -i '11,441d' $FILENAME

echo "- Remove "bullet" characters."
cat $FILENAME | perl -pe 's/ .//g' > jcr-spec.rst.tmp
mv jcr-spec.rst.tmp $FILENAME

echo "- Add spaces between section enumerations and titles"
cat $FILENAME | perl -pe 's/^([1-9.]+)([A-Z])/\1 \2/g' > jcr-spec.rst.tmp
mv jcr-spec.rst.tmp $FILENAME

echo "- Replacing image blocks with placeholders"
sed -i '/figure:: data:image/i \
.. note:: \
\
    This image is not available in this conversion of the document. Please refer to the original specification.' jcr-spec.rst
sed -i '/figure:: data:image/,+2d' $FILENAME

echo "- Adding header"

cat << EOF > $TMPFILENAME
=====================
JCR-283 Specifiaction
=====================

.. note::

    This file has been converted to RST from the \`original specification
    <https://jcp.org/aboutJava/communityprocess/final/jsr283/index.html>\`_. The
    conversion is not perfect, in particular images are not rendered.

EOF

cat $FILENAME >> $TMPFILENAME
mv $TMPFILENAME $FILENAME

echo "Installing new version"
echo "======================"

mv $FILENAME ../references/jcr-283.rst
echo ""
echo "Done!"
