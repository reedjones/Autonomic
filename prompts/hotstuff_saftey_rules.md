To ensure safety and consistency, HotStuff has two key rules:

1. If a peer sends a PREPARE vote for some block B at height H, it cannot vote for any other block at the same height.

2. If a peer sends a PRECOMMIT vote for block B at height H, it must permanently commit block B and all its ancestors.

These rules ensure that once a quorum is reached in committing a block, that decision is final and irrevocable across all honest peers.