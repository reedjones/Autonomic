Each HotStuff consensus view follows this process:

1. The current leader (initially the boot leader) multicasts a NEW_VIEW message containing the latest blockchain height and the proposed next block (e.g. proposing themselves as the new super agent).

2. Upon receiving NEW_VIEW from the leader, you (as a peer) verify:
    a) The leader is the rightful one based on the blockchain height 
    b) The proposed block extends the blockchain correctly
    c) The state in the proposed block is valid
    
3. If validations pass, you transmit a PREPARE vote for the proposed block to other peers.

4. Once a (+2/3) quorum of PREPARE votes for the same block is received from distinct peers, you multicast a PRECOMMIT vote reaching a COMMIT decision for that block.

5. Once a (+2/3) quorum of PRECOMMIT votes for the same block are received, you permanently add that block to your local blockchain copy.

6. The state from this newly committed block takes effect (e.g. the new leader becomes the super agent).

7. The leader proceeds to build the next block on top of this and transmits NEW_VIEW to start the next view.