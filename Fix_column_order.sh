awk -F'\t' -v OFS="\t" '{ print $1, $2, $3, $6, $5, $4, $7, $10, $9, $8, $11, $12 }'  reduced_8k_172020.txt > dadi_INPUT_FIXED_8K.txt
