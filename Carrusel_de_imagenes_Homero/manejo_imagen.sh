convert Fotogramas/ext_mem3.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba.txt
		
convert Fotogramas/ext_mem4.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba2.txt

convert Fotogramas/ext_mem5.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba3.txt

convert Fotogramas/ext_mem6.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba4.txt
		
convert Fotogramas/ext_mem7.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba5.txt

convert Fotogramas/ext_mem8.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba6.txt

convert Fotogramas/ext_mem9.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba7.txt
		
convert Fotogramas/ext_mem10.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba8.txt

convert Fotogramas/ext_mem11.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba9.txt

convert Fotogramas/ext_mem12.png -resize 160x80\! -depth 4 txt:- |     
		tail -n +2 | tr -cs '0-9.\n'  ' ' |       
		while read x y r g b junk; do
		   echo "$x,$y = rgb($r,$g,$b)";       
		done >Fotogramas_txt/prueba10.txt
		
python3  coloresRGB_PantallaCompleta.py

#rm prueba.txt
