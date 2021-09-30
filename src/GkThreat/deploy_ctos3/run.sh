WORK_SPACE="./"

# WORK_SPACE="/home/work_space/"

cd $WORK_SPACE
# 收集检索信息
python GkThreat/CollectFresh.py 
# 处理检索信息
python GkThreat/ExtractAddress.py :$:%d