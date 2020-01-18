#!/bin/bash

set -ue

function usage() {
    echo 'shell/setup_ch8_dataset.sh [--force]'
    exit 1
}

if [[ $# -eq 0 ]]; then
    is_force='false'
elif [[ $# -eq 1 ]]; then
    if [[ $1 = "--force" ]]; then
        is_force='true'
    else
        echo "invalid argument: $1"
        usage
        exit 1
    fi
else
    echo "invalid argument: $@"
    usage
    exit 1
fi

# nlp-knock-handsonディレクトリで実行するという前提。
# そうでない場合は一度nlp-knock-handsonに行ってから実行する
if [[ $(pwd | grep -o '/nlp-knock-handson' | wc -l) -ne 1 ]]; then
    echo "ディレクトリに nlp-knock-handson という文字列が複数あります。"
    echo "誤作成を起こすかもしれないのでなんかアレです"
    echo $(pwd)
    exit 1
fi

root_dir=$(pwd | grep -o '^.*nlp-knock-handson')
pushd $root_dir >/dev/null

data_dir=data
compression_dir=${data_dir}/compression
raw_dir=${data_dir}/raw

mkdir -p $compression_dir
mkdir -p $raw_dir

rt_polaritydata_gz=${compression_dir}/rt-polaritydata.tar.gz

if [[ ${is_force} = 'true' ]] || [[ ! -e ${rt_polaritydata_gz} ]]; then
    wget 'http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz' -O ${rt_polaritydata_gz}
else
    echo "既に ${rt_polaritydata_gz} が存在するのでダウンロードをスキップしました"
fi

tar xf ${rt_polaritydata_gz} -C ${raw_dir}


popd >/dev/null
