# prepare all the things for launching the app in Colab which is much more bothering than in a local environment

from google.colab import output  # type: ignore
import json

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
    print(json.dumps(proxied_ports))  # Print the dictionary as a JSON string
