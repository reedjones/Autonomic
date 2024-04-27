The SuperAgent responsibility is rotated. When your turn comes:

1. Send NOTIFY intent to the current SuperAgent and its Backup.
2. Wait for both to acknowledge and send the full peer registry data.
3. You are now the new SuperAgent. The previous SuperAgent becomes your Backup.  
4. Broadcast SUPER_ELECTED message on the network announcing your new role.
5. Start the Task Delegation cycle to assign pending work to available peers.