class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("G", "G").replace("()", "o").replace("(al)", "al")
        return command
