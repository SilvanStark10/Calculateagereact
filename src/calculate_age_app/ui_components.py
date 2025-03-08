"""
Custom UI components for the application.
"""
import tkinter as tk

class RoundedButton(tk.Canvas):
    """
    Custom rounded button widget for a modern UI look.
    """
    def __init__(self, parent, width, height, radius, bg, fg, text, command=None):
        """
        Create a rounded button widget.
        
        Args:
            parent: Parent widget
            width: Button width
            height: Button height
            radius: Corner radius
            bg: Background color
            fg: Text color
            text: Button text
            command: Callback function when clicked
        """
        super().__init__(parent, width=width, height=height, bg=parent["bg"],
                         highlightthickness=0, bd=0)
        self.command = command
        self.radius = radius
        self.bg = bg
        self.fg = fg
        self.text = text
        
        # Draw the rounded rectangle button
        self.create_rounded_rect(0, 0, width, height, radius, fill=bg, outline=bg)
        self.create_text(width/2, height/2, text=text, fill=fg, font=("Helvetica", 16))
        
        # Bind mouse events for clicking and cursor change
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", lambda e: self.config(cursor="hand2"))
    
    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        """
        Create a rounded rectangle shape.
        
        Args:
            x1, y1: Top-left coordinates
            x2, y2: Bottom-right coordinates
            r: Corner radius
            **kwargs: Additional arguments for the polygon
            
        Returns:
            Canvas polygon item
        """
        points = [
            x1 + r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
        
    def on_click(self, event):
        """
        Handle click events.
        
        Args:
            event: Click event
        """
        if self.command:
            self.command() 