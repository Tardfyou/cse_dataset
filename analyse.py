import json
import pandas as pd

def process_json(json_str):
    try:
        # 解析 JSON 字符串
        data = json.loads(json_str)
        
        # 提取各个字段
        instruction = data.get("instruction", "").strip()
        input_str = data.get("input", "").strip()
        output = data.get("output", "").strip()
        
        return instruction, input_str, output
    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")
        return "", "", ""

def main():
    # 读取 CSV 文件
    df = pd.read_excel('your_file.xlsx')  # 这里你需要将文件名改为你的文件名
    
    def process_row(row):
        json_str = row.get('json', '')
        instruction, input_str, output = process_json(json_str)
        
        # 更新 DataFrame
        row['instruction'] = instruction
        row['input'] = input_str
        row['output'] = output
        return row
    
    # 处理每一行数据
    df = df.apply(process_row, axis=1)
    
    # 保存到新的 Excel 文件
    df.to_excel('processed_file.xlsx', index=False)  # 这里指定处理后的文件名

if __name__ == "__main__":
    main()
