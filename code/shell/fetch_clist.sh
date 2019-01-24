rsync -zarvm --include="*/" --include="*clist.mat" --exclude="*" -e "ssh -p
$1" "$2@delbruck.caltech.edu:git/mwc_activation/data/images/$3" "$4"
