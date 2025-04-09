import os
import time
import shutil
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# フォルダ設定
INPUT_DIR = r"C:\dev\selenium_test\input"
OUTPUT_DIR = r"C:\dev\selenium_test\output"
RESULT_DIR = r"C:\dev\selenium_test\result"

# 処理済みファイルリスト
processed_files = set()

# Chromeドライバ初期化
driver = webdriver.Chrome()
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")

# フォルダがなければ作成
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

print("CSVファイルの存在を監視中...")

def process_file(filepath):
    try:
        filename = os.path.basename(filepath)
        nameonly = os.path.splitext(filename)[0]
        output_file_path = os.path.join(OUTPUT_DIR, f"{nameonly}_output.csv")
        result_file_path = os.path.join(RESULT_DIR, f"{nameonly}_output.csv")

        print(f"[INFO] 処理開始: {filename}")

        # CSV読み込み
        dataframe = pd.read_csv(filepath, header=None)
        print(f"[INFO] CSVデータ: {dataframe}")
        first_name = dataframe.iloc[0, 0]
        last_name = dataframe.iloc[0, 1]

        # 「First Name」欄に入力
        first_name_input = driver.find_element(By.ID, "firstname")
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        # 「Last Name」欄に入力
        last_name_input = driver.find_element(By.ID, "lastname")
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        # 各ラベルのtextを取得
        time.sleep(0.3)  # サーバからの応答速度に応じて要調整
        full_name_label = driver.find_element(By.XPATH, "//label[text()='Full Name']").text
        father_name_label = driver.find_element(By.XPATH, "//label[text()='Father Name']").text
        mother_name_label = driver.find_element(By.XPATH, "//label[text()='Mother Name']").text

        # outputファイルの作成(CSV)
        output_data = [full_name_label, father_name_label, mother_name_label]
        output_dataframe = pd.DataFrame([output_data])
        output_dataframe.to_csv(output_file_path, index=False, header=False, mode='a')
        print(f"[INFO] 取得データ: {output_data}")

        # resultフォルダに移動
        shutil.move(output_file_path, result_file_path)

        # 元ファイル削除
        os.remove(filepath)

        print(f"[SUCCESS] 完了: {filename}")

    except Exception as e:
        print(f"[ERROR] {filepath} の処理中にエラー: {e}")

# 監視ループ
try:
    while True:
        files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".csv")]
        for file in files:
            full_path = os.path.join(INPUT_DIR, file)
            if full_path not in processed_files:
                process_file(full_path)
                processed_files.add(full_path)
        time.sleep(1)  # 監視間隔
        # print(f"[INFO] 処理済みファイル一覧: {processed_files}")
except KeyboardInterrupt:
    driver.quit()
