#!/bin/bash

# This script sets up a Google Colab environment for running a specific project(Zank).

# 定义目录路径
FRONTEND_DIR="./frontend"
BACKEND_DIR="./backend"

# 检查前端目录是否存在
if [ ! -d "$FRONTEND_DIR" ]; then
    echo "错误：前端目录 $FRONTEND_DIR 不存在"
    exit 1
fi

# 检查后端目录是否存在
if [ ! -d "$BACKEND_DIR" ]; then
    echo "错误：后端目录 $BACKEND_DIR 不存在"
    exit 1
fi

# 检查tmux是否安装
if ! command -v tmux &> /dev/null; then
    echo "错误:tmux 未安装,请先安装tmux"
    exit 1
fi

# 创建一个新的tmux会话，命名为dev_session，不附加到会话
tmux new-session -d -s dev_session

# 在第一个窗口中进入前端目录并运行npm dev
tmux send-keys -t dev_session "cd $FRONTEND_DIR" C-m
tmux send-keys -t dev_session "npm run dev" C-m

# 创建一个新窗口（第二个窗口），进入后端目录并运行uvicorn
tmux new-window -t dev_session:1 -n "backend"
tmux send-keys -t dev_session:1 "cd $BACKEND_DIR" C-m
tmux send-keys -t dev_session:1 "uvicorn main:app --reload" C-m

# 附加到tmux会话，默认显示第一个窗口
tmux attach-session -t dev_session
    


