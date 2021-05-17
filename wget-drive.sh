
printf "Enter the drive link : "
read -r link
printf "Enter the output file name: "
read -r out
read -p "whether the file size is less than 100MB ? (Y/N) : " size

yes="Y"
no="N"

fileid=$(echo $link | cut -d "/" -f 6)

# if the size is less than 100MB - Y from input

if [[ "$size" == "$yes" ]]; then
  wget --no-check-certificate "https://docs.google.com/uc?export=download&id=$fileid" -O $out
else
  wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=$fileid' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$fileid" -O $out && rm -rf /tmp/cookies.txt
fi

