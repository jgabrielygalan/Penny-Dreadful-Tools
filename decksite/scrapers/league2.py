from decksite.data import match
from shared import dtutil

# ThereCameAHero is all over the place. His deck names don't match his two sign ups ("Devo Red" and "Dimir Control") - there is no "Black Aggro".
# 10/28/2016 22:28:39 290 ThereCameAHero    vampires    Win 2-1
# 10/28/2016 22:28:44 ThereCameAHero    290 Black Aggro Loss    1-2
# 10/29/2016 22:00:27 299 ThereCameAHero    Bant Company    Win 2-1
# Crazybaloth has no deck for this one last match despite having lots of decks, too, and again "Jund Nightmare" is not a registered deck.
# 10/29/2016 23:36:34 Therecameahero    crazybaloth Jund Nightmare    Loss    0-2

# There are no registered decks for the losing side of each of these. Best guess is that JewishGainz reported three non-league matches as league matches.
# 10/4/2016 22:52:49    245 Traeba    Bee Gees vs 8 Post    Win 2-0
# 10/7/2016 22:21:20    245 MagicFind    Bee Gees (Golgari Aggro) vs Goblins Win 2-0
# 10/8/2016 21:46:45    245 spideyjarod117    Bee Gees vs BG Ramp Win 2-1
# 10/23/2016 13:02:19 277 Chandlertron    Battle of Wits    Loss    0-2
# 10/23/2016 19:32:49 253 DrunkinAbbot    sultai emerge    Win 2-0
# 10/23/2016 20:43:36 253 EnigmaJD    sultai emerge    Win 2-1
# 10/9/2016 21:43:01    250    Abominus    Red    Win 2-1

def disabled():
    match.insert_match(dtutil.parse('10/2/2016 0:18:08', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 233, 2, 279, 0)
    match.insert_match(dtutil.parse('10/2/2016 0:28:25', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 234, 2, 231, 0)
    match.insert_match(dtutil.parse('10/2/2016 1:31:02', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 234, 2, 233, 0)
    match.insert_match(dtutil.parse('10/2/2016 3:07:38', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 231, 2, 227, 1)
    match.insert_match(dtutil.parse('10/2/2016 13:21:58', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 231, 2, 233, 0)
    match.insert_match(dtutil.parse('10/2/2016 16:42:54', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 234, 2, 232, 0)
    match.insert_match(dtutil.parse('10/2/2016 21:38:31', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 234, 2, 240, 1)
    match.insert_match(dtutil.parse('10/2/2016 21:51:14', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 239, 2, 231, 0)
    match.insert_match(dtutil.parse('10/2/2016 22:36:02', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 240, 2, 239, 0)
    match.insert_match(dtutil.parse('10/3/2016 16:25:48', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 234, 2, 228, 0)
    match.insert_match(dtutil.parse('10/3/2016 20:12:06', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 232, 2, 228, 1)
    match.insert_match(dtutil.parse('10/3/2016 20:35:35', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 242, 2, 231, 0)
    match.insert_match(dtutil.parse('10/3/2016 23:30:40', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 240, 2, 245, 0)
    match.insert_match(dtutil.parse('10/4/2016 1:59:41', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 247, 2, 246, 0)
    match.insert_match(dtutil.parse('10/4/2016 13:37:35', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 247, 2, 238, 0)
    match.insert_match(dtutil.parse('10/4/2016 18:05:12', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 248, 2, 247, 0)
    match.insert_match(dtutil.parse('10/4/2016 20:05:29', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 249, 2, 247, 1)
    match.insert_match(dtutil.parse('10/4/2016 20:59:42', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 247, 2, 282, 0)
    match.insert_match(dtutil.parse('10/5/2016 0:01:53', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 246, 2, 251, 1)
    match.insert_match(dtutil.parse('10/5/2016 2:31:44', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 248, 2, 264, 1)
    match.insert_match(dtutil.parse('10/5/2016 15:49:53', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 246, 2, 249, 1)
    match.insert_match(dtutil.parse('10/5/2016 16:19:55', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 249, 2, 248, 1)
    match.insert_match(dtutil.parse('10/5/2016 17:00:27', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 246, 2, 252, 0)
    match.insert_match(dtutil.parse('10/5/2016 17:02:56', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 248, 2, 251, 1)
    match.insert_match(dtutil.parse('10/5/2016 20:17:02', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 241, 2, 248, 1)
    match.insert_match(dtutil.parse('10/5/2016 22:38:15', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 252, 2, 253, 1)
    match.insert_match(dtutil.parse('10/6/2016 17:57:02', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 255, 2, 256, 1)
    match.insert_match(dtutil.parse('10/6/2016 18:42:06', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 257, 2, 256, 1)
    match.insert_match(dtutil.parse('10/6/2016 19:11:41', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 249, 2, 257, 0)
    match.insert_match(dtutil.parse('10/6/2016 19:24:17', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 256, 2, 258, 1)
    match.insert_match(dtutil.parse('10/6/2016 19:48:29', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 256, 2, 249, 0)
    match.insert_match(dtutil.parse('10/6/2016 21:05:31', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 256, 2, 232, 0)
    match.insert_match(dtutil.parse('10/6/2016 21:23:45', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 257, 2, 301, 0)
    match.insert_match(dtutil.parse('10/6/2016 23:42:09', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 258, 2, 260, 1)
    match.insert_match(dtutil.parse('10/7/2016 1:58:24', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 257, 2, 258, 1)
    match.insert_match(dtutil.parse('10/7/2016 6:08:27', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 255, 2, 261, 1)
    match.insert_match(dtutil.parse('10/7/2016 15:05:04', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 258, 2, 262, 0)
    match.insert_match(dtutil.parse('10/7/2016 19:35:42', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 260, 2, 254, 1)
    match.insert_match(dtutil.parse('10/8/2016 1:06:56', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 262, 2, 232, 1)
    match.insert_match(dtutil.parse('10/8/2016 1:36:57', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 260, 2, 232, 0)
    match.insert_match(dtutil.parse('10/8/2016 2:05:31', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 257, 2, 260, 0)
    match.insert_match(dtutil.parse('10/8/2016 12:06:26', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 237, 2, 245, 1)
    match.insert_match(dtutil.parse('10/8/2016 16:36:17', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 241, 2, 263, 0)
    match.insert_match(dtutil.parse('10/9/2016 13:31:10', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 241, 2, 255, 1)
    match.insert_match(dtutil.parse('10/9/2016 14:06:28', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 241, 2, 264, 0)
    match.insert_match(dtutil.parse('10/9/2016 14:24:57', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 258, 2, 241, 0)
    match.insert_match(dtutil.parse('10/10/2016 22:57:48', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 263, 2, 252, 0)
    match.insert_match(dtutil.parse('10/11/2016 16:44:16', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 261, 2, 269, 0)
    match.insert_match(dtutil.parse('10/11/2016 17:20:03', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 263, 2, 261, 0)
    match.insert_match(dtutil.parse('10/11/2016 18:56:03', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 266, 2, 261, 0)
    match.insert_match(dtutil.parse('10/11/2016 20:35:36', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 261, 2, 271, 0)
    match.insert_match(dtutil.parse('10/11/2016 21:09:15', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 263, 2, 271, 1)
    match.insert_match(dtutil.parse('10/12/2016 15:58:19', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 263, 2, 244, 0)
    match.insert_match(dtutil.parse('10/14/2016 15:23:19', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 264, 2, 267, 1)
    match.insert_match(dtutil.parse('10/15/2016 16:49:52', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 275, 2, 274, 0)
    match.insert_match(dtutil.parse('10/16/2016 6:20:41', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 275, 2, 273, 0)
    match.insert_match(dtutil.parse('10/17/2016 16:53:14', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 266, 2, 275, 0)
    match.insert_match(dtutil.parse('10/18/2016 1:03:28', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 260, 2, 268, 0)
    match.insert_match(dtutil.parse('10/18/2016 17:07:41', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 275, 2, 267, 1)
    match.insert_match(dtutil.parse('10/18/2016 17:54:29', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 275, 2, 278, 1)
    match.insert_match(dtutil.parse('10/18/2016 20:58:12', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 267, 2, 277, 0)
    match.insert_match(dtutil.parse('10/18/2016 21:21:54', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 266, 2, 279, 1)
    match.insert_match(dtutil.parse('10/18/2016 23:55:41', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 277, 2, 280, 0)
    match.insert_match(dtutil.parse('10/19/2016 0:08:47', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 251, 2, 276, 0)
    match.insert_match(dtutil.parse('10/21/2016 17:27:38', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 266, 2, 281, 1)
    match.insert_match(dtutil.parse('10/21/2016 17:58:53', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 265, 2, 264, 0)
    match.insert_match(dtutil.parse('10/22/2016 17:47:50', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 281, 2, 264, 1)
    match.insert_match(dtutil.parse('10/22/2016 19:04:44', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 281, 2, 268, 1)
    match.insert_match(dtutil.parse('10/22/2016 22:27:40', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 266, 2, 277, 0)
    match.insert_match(dtutil.parse('10/22/2016 23:05:20', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 277, 2, 273, 0)
    match.insert_match(dtutil.parse('10/23/2016 3:41:29', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 281, 2, 273, 1)
    match.insert_match(dtutil.parse('10/23/2016 3:54:56', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 281, 2, 282, 0)
    match.insert_match(dtutil.parse('10/23/2016 13:00:10', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 253, 2, 267, 1)
    match.insert_match(dtutil.parse('10/23/2016 13:12:24', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 283, 2, 280, 0)
    match.insert_match(dtutil.parse('10/23/2016 13:34:52', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 253, 2, 284, 0)
    match.insert_match(dtutil.parse('10/23/2016 14:12:30', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 267, 2, 283, 1)
    match.insert_match(dtutil.parse('10/23/2016 14:38:40', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 285, 2, 283, 0)
    match.insert_match(dtutil.parse('10/23/2016 16:09:03', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 283, 2, 286, 0)
    match.insert_match(dtutil.parse('10/23/2016 17:43:39', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 284, 2, 283, 1)
    match.insert_match(dtutil.parse('10/23/2016 18:57:13', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 284, 2, 282, 1)
    match.insert_match(dtutil.parse('10/23/2016 19:58:42', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 284, 2, 287, 0)
    match.insert_match(dtutil.parse('10/23/2016 20:32:55', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 284, 2, 288, 1)
    match.insert_match(dtutil.parse('10/23/2016 20:57:13', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 289, 2, 288, 0)
    match.insert_match(dtutil.parse('10/24/2016 0:45:48', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 289, 2, 282, 0)
    match.insert_match(dtutil.parse('10/24/2016 1:33:04', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 290, 2, 289, 0)
    match.insert_match(dtutil.parse('10/24/2016 10:25:50', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 288, 2, 285, 1)
    match.insert_match(dtutil.parse('10/24/2016 16:56:57', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 289, 2, 291, 0)
    match.insert_match(dtutil.parse('10/24/2016 17:29:46', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 282, 2, 291, 0)
    match.insert_match(dtutil.parse('10/24/2016 18:37:35', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 291, 2, 292, 1)
    match.insert_match(dtutil.parse('10/24/2016 18:57:55', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 292, 2, 289, 0)
    match.insert_match(dtutil.parse('10/24/2016 20:50:22', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 290, 2, 292, 0)
    match.insert_match(dtutil.parse('10/25/2016 17:04:42', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 291, 2, 294, 1)
    match.insert_match(dtutil.parse('10/26/2016 0:19:27', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 290, 2, 293, 0)
    match.insert_match(dtutil.parse('10/26/2016 14:23:25', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 293, 2, 295, 1)
    match.insert_match(dtutil.parse('10/26/2016 15:46:29', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 293, 2, 291, 0)
    match.insert_match(dtutil.parse('10/29/2016 5:05:18', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 298, 2, 297, 0)
    match.insert_match(dtutil.parse('10/29/2016 16:36:58', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 253, 2, 274, 0)
    match.insert_match(dtutil.parse('10/29/2016 17:32:41', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 290, 2, 274, 0)
    match.insert_match(dtutil.parse('10/30/2016 14:54:02', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 298, 2, 293, 0)
    match.insert_match(dtutil.parse('10/30/2016 22:28:49', '%m/%d/%Y %H:%M:%S', dtutil.WOTC_TZ), 293, 2, 297, 0)
