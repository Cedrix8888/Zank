import subprocess
import os

def run_commands():
    # 定义要执行的命令列表
    commands = [
        "git clone https://github.com/Cedrix8888/Zank.git",
        "cd Zank",
        "git checkout cuda",
        "python t2i.py"
    ]
    
    # 初始工作目录
    current_dir = os.getcwd()
    
    print("开始执行命令...")
    
    for i, cmd in enumerate(commands, 1):
        try:
            print(f"执行命令 {i}/{len(commands)}: {cmd}")
            
            # 对于cd命令，我们需要特殊处理以更改后续命令的工作目录
            if cmd.startswith("cd "):
                dir_path = cmd.split("cd ")[1].strip()
                new_dir = os.path.join(current_dir, dir_path)
                os.chdir(new_dir)
                current_dir = new_dir
                print(f"已切换到目录: {current_dir}")
            else:
                # 执行其他命令
                result = subprocess.run(
                    cmd, 
                    shell=True, 
                    check=True, 
                    capture_output=True, 
                    text=True,
                    cwd=current_dir
                )
                # 打印命令输出
                if result.stdout:
                    print("输出:")
                    print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"命令执行失败: {cmd}")
            print(f"错误信息: {e.stderr}")
            return
        except Exception as e:
            print(f"执行命令时发生错误: {str(e)}")
            return
    
    print("所有命令执行完毕")

if __name__ == "__main__":
    run_commands()
