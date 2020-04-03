from time import gmtime, strftime
import os
import colorama
from colorama import Fore, Style


# For coloring:
colorama.init()

class SimpLog():
    """
    This is very simple logger functionality. Be aware that YELLOW color is
    bugged in windows PowerShell. In Command Prompt colors works fine. This
    logger was also tested on Linux (Fedora).

    """

    def __init__(self, name=None, file_pth='logs.txt', append=True):
        """
        If file path provided, set it as a log file.
        Set if new logs will be appended to existing file content or the file
        will be cleared first, and then logs will be appended.

        NOTE: Leaving all arguments default will produce set-up for short logs
              appended to the file 'logs.txt' in CWD.

        Args:
        name -- Additional square brackets content. Not used by default.
        file_pth -- path to log file. If file exists and append is set to
                    false, this file will be cleared before logging
        append -- Boolean, False wil clear file before the first log entry.
        """

        # Inform user about initialization:
        now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print(f'\n{Fore.GREEN}[SETTING INFO]{Style.RESET_ALL} [START] [{now}]')

        self._name = name
        self._file_pth = file_pth
        self._mode = "Append"

        # Remove existing log file before creating new if append=False.
        if not append:
            self._mode = 'Overwrite'
            try:
                os.remove(self._file_pth)
            except FileNotFoundError:
                pass

        with open(self._file_pth, 'a') as f:
            msg1 = f'[SETTING INFO] [{now}] :: LOG FILE: {self._file_pth}'
            msg2 = f'[SETTING INFO] [{now}] :: MODE: {self._mode}'
            f.write(msg1 + '\n' + msg2 + '\n')



    def now(self):
        """Return recent date-time"""
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())

    def i(self, msg, to_file=False):
        """
        Prints an info message to the standard output (blue). Optionally
        Write this message to file with a date and time information.

        Arguments:
        msg -- user's message
        to_file -- boolean, true for file print
        """
        now = self.now()
        name = self._name
        if not self._name:
            # Log format for short line version. pline: line to print
            pline = f'{Fore.CYAN}[INFO]{Style.RESET_ALL}    :: {msg}'
            line = f'[INFO] [{now}] :: {msg}\n'
        else:
            # Log format for long line version. pline: line to print
            pline = f'{Fore.CYAN}[{name}] [INFO]{Style.RESET_ALL}    :: {msg}'
            line = f'[{name}] [INFO] [{now}] :: {msg}\n'

        print(pline)
        if to_file:
            # File entry has always the same format
            with open(self._file_pth, 'a') as f:
                f.write(line)

    def w(self, msg, to_file=False):
        """
        Prints a warning message to the standard output (yellow). Optionally
        Write this message to file with a date and time info. The yellow
        color is not properly diplayed in PowerShell (Windows 10) .

        Arguments:
        msg -- user's message
        to_file -- boolean, true for file print
        """
        now = self.now()
        name = self._name
        if not self._name:
            # Log format for short line version. plin: line to print
            plin = f'{Fore.YELLOW}[WARNING]{Style.RESET_ALL} :: {msg}'
            line = f'[WARNING] [{now}] :: {msg}\n'
        else:
            # Log format for long line version. plin: line to print
            plin = f'{Fore.YELLOW}[{name}] [WARNING]{Style.RESET_ALL} :: {msg}'
            line = f'[{name}] [WARNING] [{now}] :: {msg}\n'

        print(plin)
        if to_file:
            with open(self._file_pth, 'a') as f:
                f.write(line)

    def e(self, msg, to_file=False):
        """
        Prints an error message to the standard output (red). Optionally
        Write this message to file with a date and time information.

        Arguments:
        msg -- user's message
        to_file -- boolean, true for file print
        """
        now = self.now()
        name = self._name
        if not self._name:
            # Log format for short line version. pline: line to print
            pline = f'{Fore.RED}[ERROR]{Style.RESET_ALL}   :: {msg}'
            line = f'[ERROR] [{now}] :: {msg}\n'

        else:
            # Log format for long line version. pline: line to print
            pline = f'{Fore.RED}[{name}] [ERROR]{Style.RESET_ALL}   :: {msg}'
            line = f'[{name}] [ERROR] [{now}] :: {msg}\n'

        print(pline)
        if to_file:
            with open(self._file_pth, 'a') as f:
                f.write(line)


if __name__ == '__main__':
    """
    Just run this to test if everything is displayed correctly.
    """
    import time
    # Long format:
    lg = SimpLog(__file__, append=False)
    lg.i("This is test info msg", True)
    time.sleep(2)
    lg.i("This is test info msg", True)
    lg.w("this is warning message", True)
    lg.w("this is warning print-only message")
    lg.e("this is error message", True)
    lg.e("this is error print-only message")

    # Short format:
    lg2 = SimpLog(append=True)
    lg2.i("This is test info msg (2nd instance)", True)
    lg2.w("this is warning message (2nd instance)", True)
    lg2.w("this is warning print-only message (2nd instance)")
    lg2.e("this is error message (2nd instance)", True)
    lg2.e("this is error print-only message (2nd instance)", False)
