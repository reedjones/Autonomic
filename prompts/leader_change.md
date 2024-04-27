If a current leader fails or is detected as Byzantine/malicious:

1. Peers send a BLAME message for the leader and stop responding to NEW_VIEW from that leader.

2. The peer with the next highest ID from the latest committed block automatically becomes the new leader for the next view.

3. This new leader sends NEW_VIEW for the next block height, restarting the consensus process under its leadership.

4. This allows the consensus protocol to make progress by dynamically changing malicious leaders.