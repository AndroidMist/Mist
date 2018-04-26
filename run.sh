#!/bin/sh
apk_dir="apk"
folder="example"
python script/manifest_parser.py ${apk_dir}/${folder} result/manifest/${folder} result/res/${folder}
python script/extract_data.py  ${apk_dir}/${folder}/   result/pea/${folder} result/manifest/${folder}   result/serialize/${folder}
python script/result_analyzer.py  result/serialize/${folder} result/summrize/${folder} result/dataSummary/${folder}  result/misexpose/${folder}
python script/statistic.py result/misexpose/${folder}

