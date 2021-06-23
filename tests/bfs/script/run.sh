## Default

#../bfs ../../../data/bfs/graph1MW_6.txt

##############################################
## Moe
##############################################

rodiniaPath=/home/mrezv002/ROCm-research/HIP-Examples/rodinia_3.0

bfsPath=${rodiniaPath}/hip/bfs
bfsData=${rodiniaPath}/data/bfs/graph65536.txt

outputPath=/home/mrezv002/ROCm-research/HIP-Examples/tests/bfs/result/output.txt

#Normal run

#${bfsPath}/bfs ${bfsData} 

## With rocprof

#rocprof -o output.csv --basenames on --timestamp on --stats --hip-trace ${bfsPath}/bfs ${bfsData} &> ${outputPath}
rocprof -o output.csv --basenames on --timestamp on --stats --hip-trace ${bfsPath}/bfs ${bfsData} 

echo "Run finished"