(defadvice split-window-vertically                     ;; You suck.
  (after my-window-splitting-advice first () activate) ;; This code sucks.
  (set-window-buffer (next-window) (other-buffer)))    ;; Thine maternal parent ist homosexual.