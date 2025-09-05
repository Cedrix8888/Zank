# prepare all the things for launching the app in Colab which is much more bothering than in a local environment
# it should be run in a colab unit

from google.colab import output  # type: ignore
import re
import os
import logging

# 配置日志输出
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def update_config_files(url_5173: str, url_8000: str):
    """
    Update the configuration files with the proxy URLs.
    
    Parameters:
    url_5173: The proxy URL for port 5173
    url_8000: The proxy URL for port 8000
    """
    # Update config.js
    config_path = os.path.join('Zank/frontend', 'config.js')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            content = f.read()
        updated_content = re.sub(r"baseUrl: '[^']*'", f"baseUrl: '{url_8000}'", content)
        with open(config_path, 'w') as f:
            f.write(updated_content)
    
    # Update vite.config.js
    vite_path = os.path.join('Zank/frontend', 'vite.config.js')
    if os.path.exists(vite_path):
        with open(vite_path, 'r') as f:
            content = f.read()
        cleaned_url = url_5173.replace("https://", "")
        updated_content = content.replace("'proxy_url'", f"'{cleaned_url}'")
        with open(vite_path, 'w') as f:
            f.write(updated_content)

def port_proxy(ports: list) -> dict:
    """
    Proxy multiple ports and return a dictionary containing the ports and their corresponding accessible links.
    Parameters:
    ports: A list of ports, e.g., [5173, 3000, 8080]
    Returns:
    dict: Keys are port numbers, and values are the corresponding accessible links
    """
    
    proxy_results = {}
    
    for port in ports:
        proxy_url = output.eval_js(f"google.colab.kernel.proxyPort({port})")
        proxy_results[port] = proxy_url
    
    return proxy_results

if __name__ == "__main__":
    ports_to_proxy = [5173, 8000]  # Add more ports if needed
    proxied_ports = port_proxy(ports_to_proxy)
    
    # Update configuration files with proxy URLs
    update_config_files(proxied_ports[5173], proxied_ports[8000])
    
