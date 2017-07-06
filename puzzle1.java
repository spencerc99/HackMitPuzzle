import java.io.PrintStream;
import java.time.Instant;
import java.time.temporal.ChronoUnit;

public class puzzle1
{
  private static final long START_EPOCH = 2033292958L;

  public static void main(String[] paramArrayOfString)
  {
    Instant localInstant1 = Instant.now();
    Instant localInstant2 = Instant.ofEpochSecond(2033292958L);
    Instant localInstant3 = localInstant2.plus(1L, ChronoUnit.DAYS);

    if (true || (localInstant1.isAfter(localInstant2)) && (localInstant1.isBefore(localInstant3))) System.out.println(new Object() { int t;

        public String toString() { byte[] arrayOfByte = new byte[47]; this.t = 336726833; arrayOfByte[0] = ((byte)(this.t >>> 5)); this.t = 29267129; arrayOfByte[1] = ((byte)(this.t >>> 18)); this.t = 1787391678; arrayOfByte[2] = ((byte)(this.t >>> 5)); this.t = 545322143; arrayOfByte[3] = ((byte)(this.t >>> 24)); this.t = -413279842; arrayOfByte[4] = ((byte)(this.t >>> 2)); this.t = -1418030057; arrayOfByte[5] = ((byte)(this.t >>> 19)); this.t = -1830188587; arrayOfByte[6] = ((byte)(this.t >>> 17)); this.t = 1141678813; arrayOfByte[7] = ((byte)(this.t >>> 21)); this.t = -1705646035; arrayOfByte[8] = ((byte)(this.t >>> 22)); this.t = -1069749856; arrayOfByte[9] = ((byte)(this.t >>> 9)); this.t = 1831178324; arrayOfByte[10] = ((byte)(this.t >>> 13)); this.t = 1588101584; arrayOfByte[11] = ((byte)(this.t >>> 10)); this.t = 487131306; arrayOfByte[12] = ((byte)(this.t >>> 22)); this.t = -2014858032; arrayOfByte[13] = ((byte)(this.t >>> 1)); this.t = 926083117; arrayOfByte[14] = ((byte)(this.t >>> 15)); this.t = 1136790491; arrayOfByte[15] = ((byte)(this.t >>> 12)); this.t = 51264742; arrayOfByte[16] = ((byte)(this.t >>> 19)); this.t = -2051327895; arrayOfByte[17] = ((byte)(this.t >>> 18)); this.t = 779318182; arrayOfByte[18] = ((byte)(this.t >>> 8)); this.t = 1404928053; arrayOfByte[19] = ((byte)(this.t >>> 19)); this.t = 45273842; arrayOfByte[20] = ((byte)(this.t >>> 15)); this.t = 727131577; arrayOfByte[21] = ((byte)(this.t >>> 12)); this.t = 1376281403; arrayOfByte[22] = ((byte)(this.t >>> 20)); this.t = -790992534; arrayOfByte[23] = ((byte)(this.t >>> 8)); this.t = 732851794; arrayOfByte[24] = ((byte)(this.t >>> 13)); this.t = 1022078033; arrayOfByte[25] = ((byte)(this.t >>> 18)); this.t = 63049754; arrayOfByte[26] = ((byte)(this.t >>> 7)); this.t = -163459109; arrayOfByte[27] = ((byte)(this.t >>> 16)); this.t = 330244734; arrayOfByte[28] = ((byte)(this.t >>> 19)); this.t = 1427295950; arrayOfByte[29] = ((byte)(this.t >>> 1)); this.t = 546809509; arrayOfByte[30] = ((byte)(this.t >>> 24)); this.t = 201411641; arrayOfByte[31] = ((byte)(this.t >>> 22)); this.t = 2054110420; arrayOfByte[32] = ((byte)(this.t >>> 2)); this.t = -938929706; arrayOfByte[33] = ((byte)(this.t >>> 22)); this.t = -43228940; arrayOfByte[34] = ((byte)(this.t >>> 9)); this.t = 1048780302; arrayOfByte[35] = ((byte)(this.t >>> 12)); this.t = 1130324452; arrayOfByte[36] = ((byte)(this.t >>> 20)); this.t = -422303350; arrayOfByte[37] = ((byte)(this.t >>> 3)); this.t = 178164224; arrayOfByte[38] = ((byte)(this.t >>> 4)); this.t = 1824750132; arrayOfByte[39] = ((byte)(this.t >>> 18)); this.t = 15135315; arrayOfByte[40] = ((byte)(this.t >>> 13)); this.t = 206688437; arrayOfByte[41] = ((byte)(this.t >>> 11)); this.t = -1703746375; arrayOfByte[42] = ((byte)(this.t >>> 23)); this.t = 1217177275; arrayOfByte[43] = ((byte)(this.t >>> 5)); this.t = -1732720383; arrayOfByte[44] = ((byte)(this.t >>> 3)); this.t = -884740478; arrayOfByte[45] = ((byte)(this.t >>> 1)); this.t = -865860453; arrayOfByte[46] = ((byte)(this.t >>> 1)); return new String(arrayOfByte); }  } .toString());
    else
    {
      System.out.println("It's not your time ;)");
    }
  }
}
