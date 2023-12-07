def on_on_chat():
    pass
player.on_chat("run", on_on_chat)

agent.set_assist(PLACE_ON_MOVE, True)
agent.move(FORWARD, 5)
agent.turn(RIGHT_TURN)
agent.move(FORWARD, 3)
agent.turn(RIGHT_TURN)
agent.move(FORWARD, 5)
agent.turn(RIGHT_TURN)
agent.move(FORWARD, 3)