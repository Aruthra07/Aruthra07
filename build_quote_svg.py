import os
from datetime import date

QUOTES = [
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("Simplicity is prerequisite for reliability.", "Edsger W. Dijkstra"),
    ("Make it work, make it right, make it fast.", "Kent Beck"),
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("The most damaging phrase in the language is: 'We've always done it this way.'", "Grace Hopper"),
    ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
    ("Fix the cause, not just the symptom.", "Steve Maguire"),
    ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler"),
    ("Software is a great combination between artistry and engineering.", "Bill Gates"),
    ("Innovation distinguishes between a leader and a follower.", "Steve Jobs"),
    ("Computers are fast; developers keep them slow.", "Anonymous"),
    ("Premature optimization is the root of all evil.", "Donald Knuth"),
    ("Clean code always looks like it was written by someone who cares.", "Robert C. Martin"),
    ("Design is not just what it looks like and feels like. Design is how it works.", "Steve Jobs"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Continuous learning is the minimum requirement for success in any field.", "Denis Waitley"),
    ("AI won't replace engineers, but engineers using AI will replace those who don't.", "Anonymous"),
    ("Code is poetry written in logic.", "Anonymous"),
    ("The future belongs to those who learn more skills and combine them in creative ways.", "Robert Greene"),
    ("Technology is best when it brings people together.", "Matt Mullenweg"),
    ("Programs must be written for people to read, and only incidentally for machines to execute.", "Harold Abelson"),
    ("Experience is the name everyone gives to their mistakes.", "Oscar Wilde"),
    ("Data is the new oil, but intelligence is the engine.", "Anonymous"),
    ("Learn continuously; there's always one more thing to learn.", "Steve Jobs"),
    ("The capacity to learn is a gift; the ability to learn is a skill; the willingness to learn is a choice.", "Brian Herbert"),
    ("Strive for simplicity, embrace complexity when necessary.", "Anonymous"),
    ("Quality is not an act, it is a habit.", "Aristotle"),
    ("Action is the foundational key to all success.", "Pablo Picasso"),
    ("Small daily improvements over time lead to stunning results.", "Robin Sharma")
]

def get_daily_quote():
    day_number = date.today().toordinal()
    idx = day_number % len(QUOTES)
    return QUOTES[idx]

def generate_frameless_quote_svg(theme='dark'):
    is_dark = (theme == 'dark')
    title_color = '#38BDF8' if is_dark else '#0284C7'
    text_color = '#E2E8F0' if is_dark else '#0F172A'
    author_color = '#A78BFA' if is_dark else '#7C3AED'
    border_color = 'rgba(56,189,248,0.35)' if is_dark else 'rgba(2,132,199,0.35)'
    
    quote_text, author = get_daily_quote()

    # Font size adjustment for long quotes
    font_size = 16 if len(quote_text) < 70 else 14

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 120" width="100%" height="100%">
  <style>
    .quote-icon {{ font-family: Georgia, serif; font-size: 38px; font-weight: bold; fill: {title_color}; opacity: 0.85; }}
    
    @keyframes textShimmer {{
      0%, 100% {{ fill: {text_color}; opacity: 0.92; }}
      50% {{ fill: {title_color}; opacity: 1; }}
    }}
    
    .quote-animated {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: {font_size}px;
      font-style: italic;
      font-weight: 600;
      animation: textShimmer 4s ease-in-out infinite;
    }}
    
    .author-animated {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 13px;
      font-weight: 700;
      fill: {author_color};
      letter-spacing: 0.5px;
    }}
  </style>

  <!-- Frameless outline card -->
  <rect x="4" y="4" width="872" height="112" fill="none" stroke="{border_color}" stroke-width="1.5" rx="12"/>

  <!-- Quote Icon -->
  <text x="24" y="44" class="quote-icon">“</text>

  <!-- Animated Quote Text -->
  <text x="52" y="52" class="quote-animated">"{quote_text}"</text>
  
  <!-- Author -->
  <text x="840" y="90" text-anchor="end" class="author-animated">— {author}</text>
</svg>"""
    return svg

if __name__ == '__main__':
    with open('quote-dark.svg', 'w', encoding='utf-8') as f:
        f.write(generate_frameless_quote_svg('dark'))

    with open('quote-light.svg', 'w', encoding='utf-8') as f:
        f.write(generate_frameless_quote_svg('light'))

    quote, author = get_daily_quote()
    print(f"Generated Daily Quote SVGs successfully: '{quote}' — {author}")
