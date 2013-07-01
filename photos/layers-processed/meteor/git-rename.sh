for FILE in *; do git mv "$FILE" $(echo "$FILE" | tr " " "_"); done
