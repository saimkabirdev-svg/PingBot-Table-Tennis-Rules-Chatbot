import re
import gradio as gr

BOT_NAME = "PingBot"
RULE_SOURCE = "ITTF Laws of Table Tennis"
RULES_URL = "https://www.ittf.com/statutes/"

RULES = [
    {
        "topic": "Scoring and games",
        "keywords": ["score", "points", "11", "ten all", "10 10", "win by two", "game"],
        "answer": (
            "A game is normally won by the first player or pair to reach 11 points. "
            "At 10–10, play continues until someone leads by 2 points. "
            "A point is awarded after each rally unless the rally is a let."
        ),
    },
    {
        "topic": "Match format",
        "keywords": ["match", "best of", "how many games", "best of five", "best of seven"],
        "answer": (
            "A match consists of the best of an odd number of games. Common formats "
            "are best of 5 (first to 3 games) or best of 7 (first to 4). "
            "The event regulations determine the format being used."
        ),
    },
    {
        "topic": "Service rotation",
        "keywords": ["serve", "service turns", "two serves", "change serve", "serving order"],
        "answer": (
            "Players normally serve 2 points in a row, then service changes. "
            "At 10–10, service changes after every point. The same one-point rotation "
            "applies while the expedite system is in effect."
        ),
    },
    {
        "topic": "Choosing serve, receive, or ends",
        "keywords": ["who serves first", "choose serve", "toss", "coin toss", "ends"],
        "answer": (
            "The initial choice is decided by lot. The winner may choose to serve "
            "first, receive first, or start at a particular end. The other player "
            "gets the remaining choice."
        ),
    },
    {
        "topic": "Changing ends",
        "keywords": ["change ends", "switch sides", "ends in final game", "last game"],
        "answer": (
            "Players change ends after each game. In the deciding game, they change "
            "ends when one player or pair first reaches 5 points."
        ),
    },
    {
        "topic": "Legal service — starting position",
        "keywords": ["legal serve", "start serve", "open palm", "stationary hand"],
        "answer": (
            "The ball must rest freely on the open palm of the server’s stationary "
            "free hand before the service begins."
        ),
    },
    {
        "topic": "Legal service — toss",
        "keywords": ["toss", "throw ball", "16 cm", "six inches", "vertical"],
        "answer": (
            "The server must project the ball near vertically upward, without "
            "imparting spin, so it rises at least 16 cm after leaving the palm. "
            "It must then fall without touching anything before being struck."
        ),
    },
    {
        "topic": "Legal service — contact and bounce",
        "keywords": ["serve bounce", "where must serve land", "service bounce", "hit serve"],
        "answer": (
            "The ball must first touch the server’s court and then the receiver’s "
            "court. In doubles, it must touch the server’s right half-court and "
            "then the receiver’s right half-court."
        ),
    },
    {
        "topic": "Legal service — behind the end line",
        "keywords": ["behind line", "over table serve", "serve from where", "end line"],
        "answer": (
            "From the start of service until the ball is struck, the ball must be "
            "above the playing surface and behind the server’s end line."
        ),
    },
    {
        "topic": "Legal service — visibility",
        "keywords": ["hide ball", "hidden serve", "obscure", "visibility", "free arm"],
        "answer": (
            "The ball must not be hidden from the receiver by the server, the "
            "server’s doubles partner, or anything they wear or carry. After the "
            "ball is projected, the server’s free arm and hand must be removed "
            "from the space between the ball and the net."
        ),
    },
    {
        "topic": "Net service / let serve",
        "keywords": ["net serve", "let serve", "serve hits net", "net then lands"],
        "answer": (
            "If a serve touches the net assembly but is otherwise correct, it is "
            "a let and is replayed. There is no penalty for a correct let serve. "
            "If the serve is otherwise incorrect, it is not automatically a let."
        ),
    },
    {
        "topic": "Incorrect service",
        "keywords": ["illegal serve", "fault serve", "wrong serve", "bad service"],
        "answer": (
            "An incorrect service normally gives the opponent a point. The umpire "
            "may warn a player once when unsure whether a service action is legal; "
            "subsequent services that are not clearly legal can be penalized. "
            "For a match ruling, ask the umpire."
        ),
    },
    {
        "topic": "Singles rally order",
        "keywords": ["singles order", "who hits after serve", "return order"],
        "answer": (
            "In singles, the server serves, the receiver returns, and then the "
            "players alternate returns for the rest of the rally."
        ),
    },
    {
        "topic": "Doubles rally order",
        "keywords": ["doubles order", "partner hits", "alternating hits", "doubles rally"],
        "answer": (
            "In doubles, the server serves, the receiver returns, then the server’s "
            "partner returns, then the receiver’s partner returns. Players continue "
            "in that same order."
        ),
    },
    {
        "topic": "Doubles service and receiving order",
        "keywords": ["doubles serve order", "who receives", "doubles rotation", "partners"],
        "answer": (
            "The pair serving first chooses its first server; the receiving pair "
            "chooses its first receiver. In later games, the first receiver is the "
            "player who served to the first server in the previous game. The order "
            "of serving and receiving must be maintained."
        ),
    },
    {
        "topic": "Doubles service change",
        "keywords": ["doubles service change", "who serves next doubles", "rotation doubles"],
        "answer": (
            "In doubles, after each change of service, the previous receiver becomes "
            "the server and the server’s partner becomes the receiver. The established "
            "sequence must be followed."
        ),
    },
    {
        "topic": "What counts as a point",
        "keywords": ["win point", "point awarded", "how score point", "opponent misses"],
        "answer": (
            "You generally win a point if your opponent fails to make a correct "
            "service or return, hits the ball out or into the wrong area, obstructs "
            "the ball, deliberately hits it twice in succession, touches the net "
            "assembly, moves the playing surface, or touches the table with their "
            "free hand during the rally. There are additional specific cases in "
            "the Laws, including doubles order and some wheelchair rules."
        ),
    },
    {
        "topic": "Let",
        "keywords": ["what is a let", "let point", "replay rally", "not ready", "disturbance"],
        "answer": (
            "A let means the rally is replayed and no point is awarded. Examples "
            "include an otherwise correct serve touching the net, a receiver not "
            "being ready and not attempting the ball, an outside disturbance that "
            "affects play, or an umpire interrupting play."
        ),
    },
    {
        "topic": "Obstruction",
        "keywords": ["obstruction", "block ball", "hit before bounce", "ball passes me"],
        "answer": (
            "A player obstructs the ball if they, or anything they wear or carry, "
            "touch it while it is above or travelling toward the playing surface "
            "and it has not yet passed beyond their end line, without it having "
            "touched their court since last being struck by the opponent."
        ),
    },
    {
        "topic": "Ball in play and rally",
        "keywords": ["ball in play", "rally starts", "when rally ends"],
        "answer": (
            "The ball is in play from the last moment it is stationary on the "
            "server’s open palm before being intentionally projected for service "
            "until the rally is decided as a point or let."
        ),
    },
    {
        "topic": "Table edges and sides",
        "keywords": ["edge", "side of table", "hits side", "edge ball"],
        "answer": (
            "A ball that touches the top playing surface, including its edge, is "
            "good. A ball that touches the vertical side below the playing surface "
            "is not a valid bounce on the table."
        ),
    },
    {
        "topic": "Touching the table",
        "keywords": ["touch table", "free hand", "lean on table", "table touch"],
        "answer": (
            "During a rally, touching the playing surface with your free hand "
            "results in a point for the opponent. Touching the table with your "
            "racket hand or body is not automatically a fault, provided you do "
            "not move the playing surface or otherwise break a rule."
        ),
    },
    {
        "topic": "Touching the net",
        "keywords": ["touch net", "net touch", "racket touches net"],
        "answer": (
            "If you or anything you wear or carry touches the net assembly during "
            "a rally, your opponent wins the point."
        ),
    },
    {
        "topic": "Moving the table",
        "keywords": ["move table", "table moves", "bump table"],
        "answer": (
            "If you or anything you wear or carry moves the playing surface during "
            "a rally, your opponent wins the point."
        ),
    },
    {
        "topic": "Double hit",
        "keywords": ["double hit", "hit twice", "two contacts", "ball hits fingers"],
        "answer": (
            "Deliberately striking the ball more than once in succession is a "
            "point for the opponent. Accidental multiple contact by the racket "
            "hand in one continuous stroke is not automatically a fault under "
            "the current Laws; the umpire judges the action."
        ),
    },
    {
        "topic": "Racket requirements",
        "keywords": ["racket", "bat", "paddle", "rubber", "blade"],
        "answer": (
            "The racket may be any size, shape, or weight, but the blade must be "
            "flat and rigid. At least 85% of its thickness must be natural wood. "
            "The striking material must cover the blade within the required limits "
            "and comply with approved covering requirements."
        ),
    },
    {
        "topic": "Racket colors",
        "keywords": ["racket color", "black red", "rubber colors", "both sides"],
        "answer": (
            "One side of the racket must be black and the other a bright color "
            "clearly distinguishable from black and from the ball. Approved "
            "coverings and current color requirements should be checked for "
            "competition use."
        ),
    },
    {
        "topic": "Racket inspection and changing rackets",
        "keywords": ["change racket", "broken racket", "inspect racket", "racket check"],
        "answer": (
            "A player normally may not change their racket during a match unless "
            "it is accidentally damaged so badly that it cannot be used. The "
            "replacement racket must be shown to the opponent and umpire."
        ),
    },
    {
        "topic": "Ball specifications",
        "keywords": ["ball size", "ball weight", "table tennis ball", "40 mm"],
        "answer": (
            "The official ball is spherical, 40 mm in diameter, weighs 2.7 g, "
            "and is made of celluloid or similar plastic material. It is white "
            "or orange and matt."
        ),
    },
    {
        "topic": "Table and net dimensions",
        "keywords": ["table size", "table height", "net height", "dimensions"],
        "answer": (
            "The playing surface is 2.74 m long, 1.525 m wide, and 76 cm above "
            "the floor. The net assembly is 15.25 cm high and extends 15.25 cm "
            "beyond each side of the table."
        ),
    },
    {
        "topic": "Expedite system",
        "keywords": ["expedite", "10 minutes", "long game", "time limit"],
        "answer": (
            "The expedite system may be introduced after 10 minutes of a game "
            "unless at least 18 points have been scored, or earlier if both "
            "players or pairs request it. After it begins, players serve one "
            "point each in turn. If the receiver makes 13 correct returns in "
            "a rally, the receiver wins the point."
        ),
    },
    {
        "topic": "Intervals and breaks",
        "keywords": ["break", "interval", "rest", "between games", "time out"],
        "answer": (
            "Players are entitled to an interval of up to 1 minute between games "
            "and a brief towel break after every 6 points from the start of each "
            "game and at the change of ends in the deciding game. Each player or "
            "pair may request one time-out of up to 1 minute in an individual match. "
            "Competition regulations may specify procedures."
        ),
    },
    {
        "topic": "Advice and coaching",
        "keywords": ["coaching", "advice", "coach", "talk during match"],
        "answer": (
            "Advice may be received only during authorized intervals, such as "
            "between games or during a time-out. Advice during a rally is not "
            "allowed. The umpire may penalize unauthorized advice under the "
            "competition regulations."
        ),
    },
    {
        "topic": "Conduct and penalties",
        "keywords": ["bad behavior", "yellow card", "red card", "penalty", "swearing"],
        "answer": (
            "Players must behave fairly and respectfully. Misconduct such as "
            "abusive language, deliberate damage, or delaying play can lead to "
            "warnings and penalty points, and serious or repeated misconduct may "
            "lead to disqualification. Exact action is for the match officials."
        ),
    },
    {
        "topic": "Order errors",
        "keywords": ["wrong server", "wrong receiver", "wrong end", "order mistake"],
        "answer": (
            "If an order error is discovered, play is interrupted and corrected. "
            "Points already scored before discovery generally stand. The umpire "
            "corrects the serving, receiving, or ends order according to the Laws."
        ),
    },
    {
        "topic": "Wheelchair and para table tennis",
        "keywords": ["wheelchair", "para", "disability", "wheelchair serve"],
        "answer": (
            "Some Laws have specific wheelchair provisions, including service lets "
            "when a correct serve returns toward the net, comes to rest on the "
            "receiver’s court, or leaves the court after touching it in singles. "
            "There are also specific contact, movement, and doubles provisions. "
            "The applicable classification and competition rules matter."
        ),
    },
    {
        "topic": "Umpire and decisions",
        "keywords": ["umpire", "referee", "who decides", "challenge decision"],
        "answer": (
            "The umpire controls the match, calls points and lets, and enforces "
            "the Laws. The referee is responsible for the competition and certain "
            "decisions under the regulations. For a live match, ask the appointed "
            "official; this chatbot cannot overturn an official decision."
        ),
    },
]

# QUESTION MATCHING
def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s'-]", " ", text)
    return re.sub(r"\s+", " ", text)


def find_best_rule(question):
    """Simple keyword scoring: handles many paraphrased questions."""
    q = normalize(question)
    best_rule = None
    best_score = 0

    for rule in RULES:
        score = 0
        for keyword in rule["keywords"]:
            k = normalize(keyword)

            # Multi-word phrases count more than single words.
            if k and k in q:
                score += 2 if " " in k else 1

        if score > best_score:
            best_score = score
            best_rule = rule

    # Avoid confidently answering unrelated questions.
    if best_score == 0:
        return None

    return best_rule


def pingbot_response(message, history):
    if not message or not message.strip():
        return "Ask me a table tennis rules question and I’ll help."

    q = normalize(message)

    if q in {"hi", "hello", "hey", "assalam o alaikum", "salam"}:
        return (
            "Hello! I’m PingBot 🏓, your table tennis rules assistant. "
            "Ask me about serving, scoring, doubles, equipment, lets, or match conduct."
        )

    if q in {"thanks", "thank you", "thankyou"}:
        return "You’re welcome! Ask me another table tennis rules question anytime."

    if q in {"bye", "goodbye", "exit"}:
        return "Good game! Come back whenever you have another rules question."

    rule = find_best_rule(message)

    if rule is None:
        return (
            "I couldn’t confidently match that to a rule in my knowledge base. "
            "Try asking about service, scoring, doubles, lets, equipment, or conduct. "
            "For an official ruling, consult the match umpire or current ITTF Laws."
        )

    return (
        f"**{rule['topic']}**\n\n"
        f"{rule['answer']}\n\n"
        f"*Reference: {RULE_SOURCE}. For competition-specific details, check the "
        f"[official ITTF rules]({RULES_URL}) or ask the match umpire.*"
    )


# ============================================================
# PROFESSIONAL CHATGPT-INSPIRED FRONTEND
# ============================================================

CUSTOM_CSS = """
:root {
    --ping-accent: #0f766e;
}
.gradio-container {
    max-width: 1100px !important;
    margin: 0 auto !important;
}
#ping-header {
    text-align: center;
    padding: 22px 10px 8px;
}
#ping-header h1 {
    font-size: 2.25rem;
    font-weight: 750;
    letter-spacing: -0.04em;
    margin-bottom: 6px;
}
#ping-header p {
    font-size: 1rem;
    opacity: .78;
}
#ping-note {
    text-align: center;
    opacity: .65;
    font-size: .82rem;
    margin-top: 8px;
}
"""

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="teal",
        neutral_hue="slate",
        radius_size="lg",
    ),
    css=CUSTOM_CSS,
    title="PingBot — Table Tennis Rules",
) as demo:

    gr.HTML(
        """
        <div id="ping-header">
            <h1>🏓 PingBot</h1>
            <p>Your friendly table tennis rules assistant</p>
        </div>
        """
    )

    gr.ChatInterface(
        fn=pingbot_response,
        chatbot=gr.Chatbot(
            height=520,
            placeholder=(
                "<div style='text-align:center; opacity:.7'>"
                "<strong>Ask PingBot anything about table tennis rules</strong><br>"
                "Try: “What happens if my serve touches the net?”"
                "</div>"
            ),
        ),
        textbox=gr.Textbox(
            placeholder="Message PingBot…",
            container=False,
            scale=7,
        ),
        examples=[
            "What happens at 10–10?",
            "How high must I toss the ball on a serve?",
            "Is a serve that hits the net a point?",
            "What is the correct order in doubles?",
            "Can I touch the table during a rally?",
            "What are the official table dimensions?",
            "Explain the expedite system.",
            "What is a let?",
        ],
        title=None,
        description=None,
        submit_btn="Send",
    )

    gr.Markdown(
        f"<div id='ping-note'>"
        f"Rule reference: {RULE_SOURCE}. This assistant is educational and "
        f"does not replace match officials or event regulations."
        f"</div>"
    )


if __name__ == "__main__":
    demo.launch(
        inbrowser=True,
        share=False,
        theme=gr.themes.Soft(
            primary_hue="teal",
            neutral_hue="slate",
            radius_size="lg",
        ),
        css=CUSTOM_CSS,
    )