def get_agent_state(agent_id): """Returns the current state of a specific agent (e.g., idle, working, failed)."""
def set_agent_state(agent_id, state): """Allows an agent to update its own state in the network."""
def get_shared_state(): """Returns the current shared state of the network, including task statuses, delegation plans, and other relevant information."""
def update_shared_state(state_update):""" Allows an agent to update the shared state of the network with new information."""

