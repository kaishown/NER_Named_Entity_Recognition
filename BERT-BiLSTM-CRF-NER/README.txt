author --------yangguixiu
datatime-------20200408
python3.6
tensorflow 1.14.0 (注：不要使用tensorflow2.0版本，因为bert基于tensorflow1.0版本写的）
模型:bert+lstm-crf
----------------
训练：
命令：python3 bert_lstm_ner.py
操作：
步骤1：下载并解压预训练的bert模型 》chinese_L-12_H-768_A-12
步骤2：如果没有./bert源文件 则下载源文件 https://github.com/google-research/bert 
步骤4：检查是否有目录 ./output，没有则创建
步骤4：执行命令 python3 bert_lstm_ner.py
--------------------
模型保存在 output
------------------------------
预测：

命令 ： Python3 restful_api.py

操作：
步骤1：在testdata/t1目录中输入自己要预测的文本，每一行代表一条预测数据
步骤2：执行命令预测 Python3 restful_api.py
步骤3：在output/label_test.txt中是对应的预测结果，第三列为预测结果
