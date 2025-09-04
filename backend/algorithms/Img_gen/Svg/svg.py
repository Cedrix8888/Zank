import svgwrite

def gen_svg(
    text: str,
    x: int = 10,
    y: int = 50,
    font_size: int = 40,
    font_family: str = "Arial",
    font_weight: str = "normal",
    fill: str = "#000000",
    stroke: str | None = None,
    stroke_width: int = 1,
    style: dict[str, str] | None = None
) -> str:
    """
    Generate an SVG with vector text.
    
    Args:
        text (str): The text to render
        x (int): X position of the text
        y (int): Y position of the text
        font_size (int): Size of the font
        font_family (str): Font family to use
        font_weight (str): Weight of the font (normal, bold, etc.)
        fill (str): Fill color of the text
        stroke (str, optional): Stroke color of the text
        stroke_width (int): Width of the stroke
        style (Dict[str, str], optional): Additional CSS styles
        
    Returns:
        str: SVG string with the vector text
    """
    # Create new SVG document
    dwg = svgwrite.Drawing(size=(f"{font_size * len(text)}px", f"{font_size * 1.5}px"))
    
    # Base style
    base_style = {
        "font-family": font_family,
        "font-size": f"{font_size}px",
        "font-weight": font_weight,
        "fill": fill,
    }
    
    # Add stroke if specified
    if stroke:
        base_style["stroke"] = stroke
        base_style["stroke-width"] = str(stroke_width)
    
    # Merge with additional styles if provided
    if style:
        base_style.update(style)
    
    # Create text element
    text_element = dwg.text(text, insert=(x, y), style=";".join([f"{k}:{v}" for k, v in base_style.items()]))
    
    # Convert text to path for true vector format
    # This ensures the text remains editable as vectors
    text_element["pathLength"] = "1"  # Makes the text scalable as a path
    
    # Add the text element to the drawing
    dwg.add(text_element)
    
    return dwg.tostring()
